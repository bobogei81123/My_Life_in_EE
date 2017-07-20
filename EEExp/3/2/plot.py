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

Freq = [1e2, 1e3, 1e4, 5e4, 1e5, 2e5]
_V = np.array([
    [80/860, 750/1000, 869/1000, 432/1000, 232/1000, 152/960],
    [104/101, 104/100, 116/100, 2/10, 104/1000, 72/960],
    [112/1060, 152/1000, 396/1060, 1020/960, 1060/980, 860/940],
])
V = 20.0 * np.log10( _V )
L = ['Band pass', 'Low pass', 'High pass']
fn = [r'\SI{100}\Hz', r'\SI{1}\kHz', r'\SI{10}\kHz', 
      r'\SI{50}\kHz', r'\SI{100}\Hz', r'\SI{200}\Hz',]

for i in range(len(V)):
  X = Freq
  Y = V[i]
  # splinePlot(plt, X, Y, C[i], L[i])
  plt.semilogx(X, Y, 'o-', label=L[i])
  #plt.ylim((0, plt.ylim()[1]))
  #plt.xlim((plt.xlim()[0], plt.xlim()[1] + 0.1))

plt.xlabel('$V_{BE}$')
plt.ylabel('Gain(db) $\log (V_o/V_i)$')

plt.legend(loc=8)
plt.grid()
plt.savefig('fig1.pdf')
plt.show()

with open("data.tex", "w") as fw:
    for i in range(len(Freq)):
        fw.write('{} & {:.3f} & {:.3f} & {:.3f}\\\\\n'.format(
            fn[i], _V[0][i], _V[1][i], _V[2][i]))

with open("ngspice/sim.data") as f:
    raw = f.read();
    _D = list(map(lambda x: x.split(), raw.strip().split('\n')))
    D = np.array(_D).T

    for i in range(0, 6, 2):
        X = D[i]
        Y = D[i+1]
        plt.semilogx(X, Y, '-', label=L[i//2])
    plt.legend(loc=8)
    plt.grid()
    plt.savefig('fig2.pdf')
    plt.show()

with open("ngspice/des.data") as f:
    raw = f.read();
    _D = list(map(lambda x: x.split(), raw.strip().split('\n')))
    D = np.array(_D).T

    X = D[0]
    Y = D[1]
    plt.semilogx(X, Y, '-', label=L[0])
    plt.legend(loc=8)
    plt.grid()
    plt.savefig('fig3.pdf')
    plt.show()
        
  
  


