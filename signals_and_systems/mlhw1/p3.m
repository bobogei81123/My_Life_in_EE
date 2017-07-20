x1 = ones(1, 500);
x2 = ones(1, 500);

y = my1conv(x1, x2);
stem(y);
print -djpg p4.jpg % Save fig to p4.jpg
pause();
