alpha = 48000/2;
beta = 180/pi;

[b, a] = ellip(10, 1, 40, [18 20]/24);
[H, w] = freqz(b, a, 10000);
plot(alpha*w, 20*log10(abs(H)));
%print(['fig'  '4-1.eps'], '-color')
plot(alpha*w, beta*angle(H));
%print(['fig'  '4-2.eps'], '-color')
ys = impz(b, a);
plot(ys);
%print(['fig'  '4-3.eps'], '-color')

[b, a] = cheby2(10, 40, [18 20]/24);
[H, w] = freqz(b, a, 10000);
plot(alpha*w, 20*log10(abs(H)));
%print(['fig'  '5-1.eps'], '-color')
plot(alpha*w, beta*angle(H));
%print(['fig'  '5-2.eps'], '-color')
ys = impz(b, a);
plot(ys);
%print(['fig'  '5-3.eps'], '-color')

