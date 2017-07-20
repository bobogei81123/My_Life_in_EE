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

mpl.rc('font', size=18)

F = []
AD = []
ACM = []
CMRR = []

with open('ad.data') as f:
    while True:
        raw = f.readline()
        if not raw: break
        fr, y1, y2 = map(float, raw.split())
        F.append(fr)
        AD.append(y1/0.02)
        ACM.append(y2/1000)
        CMRR.append(np.log(20*AD[-1]/ACM[-1]))

plt.loglog(F, AD, '-o')
plt.grid()
#plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=2, borderaxespad=0.)
plt.xlabel('Frequency \si{\hertz}')
plt.ylabel('$A_d$')
plt.savefig('fig_ad.pdf')
plt.show()
  
plt.loglog(F, ACM, '-o')
plt.grid()
#plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=2, borderaxespad=0.)
plt.xlabel('Frequency \si{\hertz}')
plt.ylabel(' $\log A_{cm}$')
plt.savefig('fig_acm.pdf')
plt.show()

plt.plot(F, CMRR, '-o')
plt.semilogx()
plt.grid()
#plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=2, borderaxespad=0.)
plt.xlabel('Frequency \si{\hertz}')
plt.ylabel('CMRR')
plt.savefig('fig_cmrr.pdf')
plt.show()
