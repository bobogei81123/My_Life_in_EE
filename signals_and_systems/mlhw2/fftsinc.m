function y = fftsinc()
    N = 1001;
    N1 = 500;
    T = 100;
    Ts = T / N;
    function [_x, _Xf] = calc(K)
        M = N1 * K;
        rg = -M:M;
        rrg = Ts * rg;
        function _y = sinc(t)
            _y = sin(pi * t) ./ (pi * t);
        end
        _x = sinc(rrg);
        %print -djpg p1.jpg; % Save fig to p1.jpg
        _Xf = abs(fftshift(fft(_x)));
    end
    [x, Xf] = calc(1);
    plot(rg, x);
    %print -djpg p1.jpg; % Save fig to p1.jpg
    plot(rg, Xf);
    %print -djpg p2.jpg; % Save fig to p2.jpg

    [x, Xf] = calc(16);
    plot(rg, x);
    %print -djpg p3.jpg; % Save fig to p3.jpg
    plot(rg, Xf);
    %print -djpg p4.jpg; % Save fig to p4.jpg
end
