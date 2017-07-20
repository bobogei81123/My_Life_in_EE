import matplotlib
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, splrep, splev, pchip
import numpy as np

C = ['green', 'blue', 'red', 'purple']

def splinePlot(p, X, Y, cl):
  p.plot(X, Y, 'o', mfc=cl, c=cl)
  #f = interp1d(X, Y, kind='pchip')
  #f = splrep(X, Y, s=0)
  f = pchip(X, Y)
  nx = np.linspace(X[0], X[-1], 100)
  ny = [f(x) for x in nx]
  p.plot(nx, ny, '-', color=cl)

matplotlib.rc('font', size=15)

Vbe = [0, 0.05, 0.1, 0.15, 0.20, 0.25, 0.3, 0.35, 0.4, 0.45, 0.51,
       0.55, 0.60, 0.65, 0.71, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0,
       1.04, 1.11, 1.16, 1.2, 1.5, 2, 2.5, 3., 4., 5., 6.]
I = [
  0.012, 0.27, 0.48, 0.655, 0.841, 0.996, 1.172, 1.357, 1.530, 1.680, 1.828,
  1.976, 2.132, 2.269, 2.422, 2.554, 2.683, 2.814, 2.946, 3.09, 3.25, 3.31,
  3.48, 3.59, 3.68, 4.35, 5.2, 5.8, 6.228, 6.57, 6.69, 6.73
]

X = Vbe
Y = I
splinePlot(plt, X, Y, 'blue')
#plt.plot(X, Y, 'o-')
#plt.ylim((0, plt.ylim()[1]))
#plt.xlim((plt.xlim()[0], plt.xlim()[1] + 0.1))
plt.xlabel('$V_{GS}$')
plt.ylabel('$I_D$')
plt.grid()

plt.savefig('fig2.pdf')
plt.show()
  
  


