M = 1000;
f1 = 100;
Ts = 0.002;
ns = 1:M;

xs = cos(2*pi*(ns-1)*Ts) + cos(2*pi*f1*(ns-1)*Ts);

L = 16;

[b, a] = butter(L, 0.2);
ys = filter(b, a, xs);
plot(ns, ys);
%print('fig6.eps', '-color')

[b, a] = cheby2(L, 40, [0.2, 0.8]);
ys = filter(b, a, xs);
plot(ns, ys);
%print('fig7.eps', '-color')
