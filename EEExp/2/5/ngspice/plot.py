import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, splrep, splev, pchip
import numpy as np

params = {'text.usetex': True, 
          'text.latex.unicode': True,
          'text.latex.preamble': [r'\usepackage{siunitx}', r'\usepackage{amsmath}', ]}
mpl.rcParams.update(params)
mpl.rc('font', size=18)

F = []
DB = []
A = []
R = []

with open('ad.data') as f:
    while True:
        raw = f.readline()
        if not raw: break
        dt = list(map(float, raw.split()))
        F.append(dt[0])
        DB.append(dt[1])
        A.append(dt[3])
        R.append(dt[5]/1000000)

plt.plot(F, DB, '-')
plt.semilogx()
plt.grid()
#plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=2, borderaxespad=0.)
plt.xlabel('Frequency \si{\hertz}')
plt.ylabel('dB = $20 \log A_d$')
plt.savefig('ad_db.pdf')
plt.show()
  
plt.plot(F, R, '-')
plt.semilogx()
plt.grid()
#plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=2, borderaxespad=0.)
plt.xlabel('Frequency \si{\hertz}')
plt.ylabel('$R_{id} \quad(\si{\mega\ohm})$')
plt.savefig('ad_r.pdf')
plt.show()

V1 = []
V2 = []

with open('ad2.data') as f:
    while True:
        raw = f.readline()
        if not raw: break
        dt = list(map(float, raw.split()))
        V1.append(dt[1])
        V2.append(dt[3])

plt.plot(V1, V2)
plt.grid()
#plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=2, borderaxespad=0.)
plt.xlabel('Input voltage $v_{i}$')
plt.ylabel('Output voltage $v_{o}$')
plt.savefig('ad_vv.pdf')
plt.show()

F = []
DB = []
A = []
R = []

with open('acm.data') as f:
    while True:
        raw = f.readline()
        if not raw: break
        dt = list(map(float, raw.split()))
        F.append(dt[0])
        DB.append(dt[1])
        R.append(dt[3]/1000000)

plt.plot(F, DB, '-')
plt.semilogx()
plt.grid()
#plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=2, borderaxespad=0.)
plt.xlabel('Frequency \si{\hertz}')
plt.ylabel('dB = $20 \log A_{cm}$')
plt.savefig('acm_db.pdf')
plt.show()
  
plt.plot(F, R, '-')
plt.semilogx()
plt.grid()
#plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=2, borderaxespad=0.)
plt.xlabel('Frequency \si{\hertz}')
plt.ylabel('$R_{id} \quad(\si{\mega\ohm})$')
plt.savefig('acm_r.pdf')
plt.show()


F = []
DB = []
A = []
R = []

with open('acmr200.data') as f:
    while True:
        raw = f.readline()
        if not raw: break
        dt = list(map(float, raw.split()))
        F.append(dt[0])
        DB.append(dt[1])
        R.append(dt[3]/1000000)

plt.plot(F, DB, '-')
plt.semilogx()
plt.grid()
#plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=2, borderaxespad=0.)
plt.xlabel('Frequency \si{\hertz}')
plt.ylabel('dB = $20 \log A_{cm}$')
plt.savefig('acmr200_db.pdf')
plt.show()
  
plt.plot(F, R, '-')
plt.semilogx()
plt.grid()
#plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=2, borderaxespad=0.)
plt.xlabel('Frequency \si{\hertz}')
plt.ylabel('$R_{id} \quad(\si{\mega\ohm})$')
plt.savefig('acmr200_r.pdf')
plt.show()

