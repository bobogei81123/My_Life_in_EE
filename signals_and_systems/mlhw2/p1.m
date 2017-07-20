x1 = zeros(1, 1000);

for i = 1:1000
    if i <= 500
        x1(i) = i;
    elseif i <= 999
        x1(i) = 999 - i + 1;
    else
        x1(i) = 0;
    end
end
stem(x1)
print -djpg p1.jpg % Save fig to p1.jpg
pause()

x2 = [ones(1, 500), zeros(1, 500)];
stem(x2)
print -djpg p2.jpg % Save fig to p2.jpg
pause()

y = conv(x1, x2);

stem(y)
print -djpg p3.jpg % Save fig to p3.jpg
pause()
