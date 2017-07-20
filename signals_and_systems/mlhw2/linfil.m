function y = linfil()
    MX = 60;

    function _s = gets(n)
        _s = 5 * sin((pi / 10) .* n + 3) .* (n >= 0);
    end

    function _sf = filt(_x, _b, _N)
        len = size(_x, 2);
        z = [zeros(1, _N-1), _x];
        a = zeros(1, _N);
        a(1) = (1 - _b) / (1 - _b^_N);
        for i = 2:_N
            a(i) = a(i-1) * _b;
        end
        a = a(N:-1:1);
        _sf = zeros(1, len);
        for i = 1:len
            _sf(i) = sum(z(i:i+_N-1) .* a);
        end
    end

    rg = 0:MX;
    s = gets(rg);
    v = randn(1, 61);
    x = s + v;

    b = 0.2;
    N = 3;
    plot(x);
    print -djpg p5.jpg; % Save fig to p5.jpg
    sf = filt(x, b, N);
    plot(rg, x, '--b', rg, sf, '-r');
    legend('origin', 'after filter');
    print -djpg p6.jpg; % Save fig to p6.jpg

    b = 0.2;
    N = 10;
    plot(x);
    print -djpg p7.jpg; % Save fig to p7.jpg
    sf = filt(x, b, N);
    plot(rg, x, '--b', rg, sf, '-r');
    legend('origin', 'after filter');
    print -djpg p8.jpg; % Save fig to p8.jpg

    b = 0.5;
    N = 3;
    plot(x);
    print -djpg p9.jpg; % Save fig to p9.jpg
    sf = filt(x, b, N);
    plot(rg, x, '--b', rg, sf, '-r');
    legend('origin', 'after filter');
    print -djpg p10.jpg; % Save fig to p10.jpg
end
