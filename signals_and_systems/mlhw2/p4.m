x1 = ones(1, 500);
x2 = ones(1, 1001);

y = my2conv(x1, x2);
stem(y);
print -djpg p5.jpg % Save fig to p5.jpg
pause();
