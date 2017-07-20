%pkg load signal
z1 = -1;
z2 = 1;
A = 0.0976;

p1 = [1 -z1];
p2 = [1 -z2];

b = A * conv( conv( p1, p1 ) , conv(p2, p2) );

y1 = 0.3575 + 0.5889i;
y2 = conj(y1);
y3 = 0.7686 + 0.3338i;
y4 = conj(y3);

q1 = [1 -y1];
q2 = [1 -y2];
q3 = [1 -y3];
q4 = [1 -y4];

a = conv( conv( q1, q2 ) , conv( q3, q4 ) );
[r, p, k] = residuez(b, a)

zplane(roots(b), roots(a));
%print('fig1.eps', '-color');

[h, w] = freqz(b, a, 10000);
plot(w,20*log10(abs(h)));
xlabel('Frequency')
ylabel('Magnitude (dB)')
%print('fig2-1.eps', '-color');

plot(w,180*arg(h)/pi);
xlabel('Frequency')
ylabel('Magnitude (dB)')
%print('fig2-2.eps', '-color');

[sos, g] = zp2sos(roots(b), roots(a))
b1 = sos(1, 1:3);
a1 = sos(1, 4:6);
b2 = sos(2, 1:3);
a2 = sos(2, 4:6);

[h, w] = freqz(b1, a1, 10000);
plot(w,20*log10(abs(h)));
xlabel('Frequency')
ylabel('Magnitude (dB)')
%print('fig3.eps', '-color');

[h, w] = freqz(b2, a2, 10000);
plot(w,20*log10(abs(h)));
xlabel('Frequency')
ylabel('Magnitude (dB)')
%print('fig4.eps', '-color');

[y, t] = impz(b, a);
plot(t, y);
%print('fig5.eps', '-color');


