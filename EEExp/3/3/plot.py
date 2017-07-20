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

VA = [.23, .216, .186, .144, .113, .07, .033, 
      -.005, -.014, -.022, -.042, -.029, -.033, 
      -.035, -.039, -.040, -.043, -.046, -.062, 
      -.075, -.096, -.115, -.128, -.173, -.158, 
      -.187, ]

VE = [ -7.6, -7.59, -7.56, -7.50, -7.44, -7.27, 
    -6.84, -6.00, -5.74, -5.59, -5.09, -5.31, 
    -5.21, -5.12, -5.06, -5.02, -4.941, -4.864, 
    -4.447, -4.123, -3.55, -3.10, -2.99, -1.71, 
    -2.08, -1.41, ]

VF = [ 8.02, 8.01, 8.01, 8.01, 8.01, 8.01, 8.005,
    7.63, 7.39, 7.04, 0.2, 5.35, 3.28, 1.08, -0.72,
    -1.98, -4.01, -6.0, -7.25, -7.385, -7.50, -7.551,
    -7.58, -7.64, -7.627, -7.658, ]

VA, VE, VF = map(list, zip(*sorted(zip(VA, VE, VF))))
print(sorted(zip(VA, VE, VF)))


# plt.plot(VA, VE)
splinePlot(plt, VA, VE, 'red', '$V_E$')
splinePlot(plt, VA, VF, C[1], '$V_F$')
  # plt.semilogx(X, Y, 'o-', label=L[i])
  #plt.ylim((0, plt.ylim()[1]))
  #plt.xlim((plt.xlim()[0], plt.xlim()[1] + 0.1))

plt.xlabel('$V_{A}$')
plt.ylabel('Voltage $V$')

plt.legend(loc=7)
plt.grid()
plt.savefig('fig1.pdf')
plt.show()

F = [1e3, 2e3, 5e3, 10e3, 20e3, 50e3, 100e3, 200e3, 500e3, 1e6, 2e6]
A = [11/18.6, 11.2/18.4, 11.04/18.4, 10.72/18.4, 9.4/18.4, 5.2/17.8, 2.64/18.0, 1.221/17.4,
     0.32/15.0, 0.144/16.6, 0.028/14.0]
A = 20*np.log10(1000*np.array(A))

plt.semilogx(F, A, '-o')

plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain(dB) $\log (V_o/V_i)$')

plt.savefig('fig2.pdf')
plt.show()
