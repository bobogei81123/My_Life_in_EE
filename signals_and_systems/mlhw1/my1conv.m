function y = my1conv(x1, x2)
    l1 = size(x1, 2);
    l2 = size(x2, 2);
    ly = l1 + l2 - 1;
    y = zeros(1, ly);

    for i = 2:ly+1
        for j = max(1, i-l2):min(i-1, l1)
            y(i-1) += x1(j) * x2(i-j);
        end
    end
end
