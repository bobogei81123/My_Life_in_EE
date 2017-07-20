import matplotlib
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, splrep, splev, pchip
import numpy as np

C = ['green', 'blue', 'red', 'purple']

def splinePlot(p, X, Y, cl, l):
  p.plot(X, Y, 'o', mfc=cl, c=cl)
  #f = interp1d(X, Y, kind='pchip')
  #f = splrep(X, Y, s=0)
  f = pchip(X, Y)
  nx = np.linspace(X[0], X[-1], 100)
  ny = [f(x) for x in nx]
  p.plot(nx, ny, '-', color=cl, label=l)

matplotlib.rc('font', size=15)

Vbe = [0, 0.05, 0.1, .15, .2, .5, 1., 2.]
I = [
  [.155, 1.952, 4.302, 5.675, 5.900, 5.998, 6.06, 6.117],
  [0.322, 3.538, 7.579, 10.48, 11.69, 12.0, 12.23, 12.40],
  [0.5, 5.236, 11.217, 15.619, 17.908, 18.869, 19.088, 19.463],
  [.678, 6.488, 13.701, 19.48, 24.766, 25.11, 25.484, 26.034],
]
L = ['$V = 0.9$', '$V = 1.2$', '$V = 1.5$', '$V = 1.8$']

for i in range(len(I)):
  X = Vbe
  Y = [0] + [ z - I[i][0] for z in I[i] ][1:]
  splinePlot(plt, X, Y, C[i], L[i])
  #plt.plot(X, Y, 'o-')
  #plt.ylim((0, plt.ylim()[1]))
  #plt.xlim((plt.xlim()[0], plt.xlim()[1] + 0.1))
  plt.xlabel('V_{BE}')
  plt.ylabel('Gain(db) $\log (V_o/V_i)$')

plt.legend()
plt.grid()
plt.savefig('fig1.pdf')
plt.show()
  
  


