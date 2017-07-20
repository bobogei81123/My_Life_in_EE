import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, splrep, splev, pchip
import numpy as np

params = {'text.usetex': True, 
          'text.latex.unicode': True,
          'text.latex.preamble': [r'\usepackage{siunitx}', r'\usepackage{amsmath}', ]}
mpl.rcParams.update(params)

C = ['green', 'blue', 'red', 'purple']

def splinePlot(p, X, Y, cl, l):
  p.plot(X, Y, 'o', mfc=cl, c=cl)
  #f = interp1d(X, Y, kind='pchip')
  #f = splrep(X, Y, s=0)
  f = pchip(X, Y)
  nx = np.linspace(X[0], X[-1], 100)
  ny = [f(x) for x in nx]
  p.plot(nx, ny, '-', color=cl, label=l)

#mpl.rc('font', size=15)

F = [500] + [ x*y for y in [1e3, 1e4, 1e5] for x in [1, 2, 5]]
A = [
    [80/266, 80/264, 80/266, 80/266, 80/262, 80/260, 78/260, 76/260, 70/260, 50/260],
    [90/266, 90/264, 90/262, 90/260, 92/262, 88/260, 88/258, 84/258, 76/258, 52/258],
    [244/266, 244/264, 244/266, 244/266, 244/260, 238/260, 172/200, 144/200, 100/200, 50/198],
    [740/21.6, 800/21.6, 840/21.6, 840/21.6, 820/21.6, 820/21.2, 780/21.2, 720/20.8, 600/20.4, 324/22.0],
    [840/21.6, 900/22.0, 920/21.6, 940/21.6, 920/21.2, 900/20, 880/20.8, 800/20, 632/20, 336/22],
    [224/2.14, 230/2.16, 234/2.14, 232/2.12, 230/2.12, 226/2.14, 200/2.10, 148/2.04, 86/2.00, 36/2.00],
]
L = ['\\SI{47}{\\kilo\\ohm}', '\\SI{56}{\\kilo\\ohm}', '\\infty'] * 2
#L = [''] * 6

plt.figure().add_axes([0.1, 0.25, 0.8, 0.65])
for i in range(len(A)):
    print(F)
    s = 'without C' if i < 3 else 'with C'
    plt.loglog(F, A[i], 's-', label=r'$R = {}$, {}'.format(L[i], s))

plt.grid()
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=2, borderaxespad=0.)
plt.savefig('fig1.pdf')
plt.show()
  
  


