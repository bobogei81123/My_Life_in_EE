function y = my2conv(x1, x2)
    l1 = size(x1, 2);
    l2 = size(x2, 2);
    ly = l1 + l2 - 1;
    A = zeros(ly, l2);

    for i = 1:l1
        for j = 1:l2
            A(i+j-1, j) = x1(i);
        end
    end
    y = (A * x2')';
end
