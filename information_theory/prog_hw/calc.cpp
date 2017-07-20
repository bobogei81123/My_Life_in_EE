#include<bits/stdc++.h>
using namespace std;
#define FZ(n) memset((n),0,sizeof(n))
#define FMO(n) memset((n),-1,sizeof(n))
#define MC(n,m) memcpy((n),(m),sizeof(n))
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define ALL(x) begin(x),end(x)
#define IOS do { ios_base::sync_with_stdio(0);cin.tie(0); } while (0)
#define SZ(x) ((int)(x).size())
#ifndef OFFLINE
    #define ONLINE_JUDGE
#endif
#ifdef ONLINE_JUDGE
#define FILEIO(name) \
    do { \
        freopen(name".in", "r", stdin); \
        freopen(name".out", "w", stdout); \
    } while (0)
#else
    #define FILEIO(name) do { } while(0)
#endif

#define _TOKEN_CAT2(x, y) x ## y
#define _TOKEN_CAT(x, y) _TOKEN_CAT2(x, y)
#define _MACRO_OVERL3(_1, _2, _3, _N, ...) _N
#define _RANGE1(a) int _TOKEN_CAT(_t, __LINE__)=0; _TOKEN_CAT(_t, __LINE__)<(a); (_TOKEN_CAT(_t, __LINE__))++
#define _RANGE2(i, a) int (i)=0; (i)<(a); (i)++
#define _RANGE3(i, a, b) int (i)=(a); (i)!=(b); (i)+=((b)>(a)?1:-1)
#define loop(...) for (_MACRO_OVERL3(__VA_ARGS__, _RANGE3, _RANGE2, _RANGE1)(__VA_ARGS__))

#ifdef OFFLINE
template<typename T>
void _dump(const char* s, T&& head) { 
    cerr << s << " = " << head << " <<" << endl; 
}

template<typename T, typename... Args>
void _dump(const char* s, T&& head, Args&&... tail) {
    int c = 0;
    while (*s!=',' || c!=0) {
        if (*s=='(' || *s=='[' || *s=='{' || *s=='<') c++;
        if (*s==')' || *s==']' || *s=='}' || *s=='>') c--;
        cerr << *s++;
    }
    cerr << " = " << head << ", ";
    _dump(s+1, tail...);
}

#define dump(...) do { \
    cerr << "\033[32m>> " << __LINE__ << ": " << __PRETTY_FUNCTION__ << endl; \
    cout << "   "; \
    _dump(#__VA_ARGS__, __VA_ARGS__); \
    cout << "\033[0m"; \
} while (0)
#else
#define dump(...) 
#endif

#define au auto
template<class T>
using vec = vector<T>;

template<typename Iter>
ostream& _IterOutput_(ostream &o, Iter b, Iter e, const string ss="", const string se="") {
    o << ss;
    for (auto it=b; it!=e; it++) o << (it==b ? "" : ", ") << *it;
    return o << se;
}

template<typename T1, typename T2>
ostream& operator << (ostream &o, const pair<T1, T2> &pair) {
    return o << "(" << pair.F << ", " << pair.S << ")";
}

template<typename T>
ostream& operator << (ostream &o, const vector<T> &vec) {
    return _IterOutput_(o, ALL(vec), "[", "]");
}

template<typename T>
ostream& operator << (ostream &o, const set<T> &st) {
    return _IterOutput_(o, ALL(st), "{", "}");
}

template<typename T, size_t N>
ostream& operator << (ostream &o, const array<T, N> &arr) {
    return _IterOutput_(o, ALL(arr), "|", "|");
}

template<typename T1, typename T2>
ostream& operator << (ostream &o, const map<T1, T2> &mp) {
    o << "{";
    for (auto it=mp.begin(); it!=mp.end(); it++) {
        o << (it==mp.begin()?"":", ") << it->F << ":" << it->S;
    }
    o << "}";
    return o;
}

using pdd = pair<double, double>;

const double P = 0.3;

inline void do_xor(int k, int d, int *u) {
    for (int i=0, p=0; i+1<k; i+=2, p+=2*d)
        u[p] ^= u[p+d];
}

// Calculate P^(n)(0|u[0..k-1]), P^(n)(1|u[0..k-1])
pdd prob(int n, int k, int d, int *u) {
    if (n == 1) {
        assert(k == 0);
        return {1-P, P};
    }

    do_xor(k, d, u);
    pdd ans;
    int kk = k / 2;
    // k Even
    if (k % 2 == 0) {
        pdd pe = prob(n/2, kk, d+d, u);
        pdd po = prob(n/2, kk, d+d, u+d);
        ans = {po.F*pe.F + po.S*pe.S, po.F*pe.S + po.S*pe.F};
    } else { // k Odd
        int t = u[d*(k-1)];
        pdd pe = prob(n/2, kk, d+d, u);
        pdd po = prob(n/2, kk, d+d, u+d);
        if (t) {
            double q = pe.S*po.F + pe.F*po.S;
            ans = {pe.S*po.F/q, pe.F*po.S/q};
        } else {
            double q = pe.F*po.F + pe.S*po.S;
            ans = {pe.F*po.F/q, pe.S*po.S/q};
        }
    }
    do_xor(k, d, u);
    return ans;
}

const int MX = 66000;
int N;
int U[MX];
int X[MX];

void go(int n, int *x) {
    if (n == 1) return;

    int nf = n/2;
    go(nf, x);
    go(nf, x+nf);

    for (int i=0; i<nf; i++) {
        x[i] ^= x[nf+i];
    }
}

const double EPS = 1e-15;
double H(double p) {
    return -p * log2(p+EPS) + -(1-p)*log2(1-p+EPS);
}

void shift(int n, int *x) {
    int l = __lg(n);
    for (int i=0; i<n; i++) {
        int j = 0;
        for (int t=0, a=i; t<l; t++) {
            j *= 2;
            j |= a&1;
            a /= 2;
        }
        if (i < j) swap(x[i], x[j]);
    }
}

double hao[2] = {};
int Y[MX];
int Z;
void sea(int n, int k, double p) {
    if (k == n) {
        for (int i=0; i<n; i++) X[i] = Y[i];
        go(n, X);
        shift(n, X);
        for (int i=0; i<Z; i++) if (X[i] != U[i]) return;

        hao[X[Z]] += p;
        return;
    }

    Y[k] = 0;
    sea(n, k+1, p*(1-P));
    Y[k] = 1;
    sea(n, k+1, p*P);
}

int32_t main(int argc, char* argv[]) {
    IOS;
    N = atoi(argv[1]);

    int ql = 0, qr = N;
    if (argc == 3) {
        ql = atoi(argv[1]);
        qr = atoi(argv[2]);
    }

    const int T = 100000;
    std::default_random_engine gen;
    std::bernoulli_distribution distri(P);
    cout << fixed << setprecision(6);

    double tot = 0.0;
    for (int k=ql; k<qr; k++) {
        double ex = 0.0;
        for (int _=0; _<T; _++) {
            for (int i=0; i<N; i++) U[i] = distri(gen);
            go(N, U);
            int l = __lg(N);
            for (int i=0; i<N; i++) {
                int j = 0;
                for (int t=0, a=i; t<l; t++) {
                    j *= 2;
                    j |= a&1;
                    a /= 2;
                }
                if (i < j) swap(U[i], U[j]);
            }

            pdd p = prob(N, k, 1, U);
            ex += H(p.F);
        }

        double pp = ex / T;
        cout << N << "," << k << "," << pp << endl;
        tot += ex / T;
        //if (0.01 <= pp && pp <= 0.99)
            //cout << k << " : " << pp << endl;
    }
    cout << endl;

    return 0;
}

