pkg load signal

rg = 1:100;
fs = 10;
Ts = 1/fs;
x = cos(2*pi*(rg-1)*Ts);

function proc(L_, fc_, rg_, x_, ss)
    L = L_; fc = fc_;
    [b, a] = butter(L, fc);

    [H, w] = freqz(b, a, 10000);
    plot(w*5/pi, 20*log10(abs(H)));
    xlabel('Normalized Frequency (*pi rad/sample)')
    ylabel('Magnitude (dB)')
    %print(['fig' ss '-1.eps'], '-color')

    plot(w*5/pi, angle(H) * 180 / pi);
    xlabel('Normalized Frequency (*pi rad/sample)')
    ylabel('Angle (degree)')
    %print(['fig' ss '-2.eps'], '-color')

    xp = filter(b, a, x_);
    plot(rg_, x_, ':b', xp, '-r');
    legend('Origin x[n]', 'After filter x[n]')
    %print(['fig' ss '-3.eps'], '-color')
end

proc(3, 0.1, rg, x, '1')
proc(7, 0.1, rg, x, '2')
proc(3, 0.5, rg, x, '3')

