import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, splrep, splev, pchip
import numpy as np

params = {'text.usetex': True, 
          'text.latex.unicode': True,
          'text.latex.preamble': [r'\usepackage{siunitx}', r'\usepackage{amsmath}', ]}
mpl.rcParams.update(params)
mpl.rc('font', size=18)

V1 = []
V2 = []
I = []

with open('p1bad.data') as f:
    while True:
        raw = f.readline()
        if not raw: break
        dt = list(map(float, raw.split()))
        V1.append(dt[1])
        V2.append(dt[3])

plt.plot(V1, V2)
plt.grid()
plt.xlabel('Input voltage $v_{i}$')
plt.ylabel('Output voltage $v_{o}$')
plt.savefig('p1vvbad.pdf')
plt.show()

V1 = []
V2 = []
I = []

with open('p1.data') as f:
    while True:
        raw = f.readline()
        if not raw: break
        dt = list(map(float, raw.split()))
        V1.append(dt[1])
        V2.append(dt[3])
        I.append(dt[5])

plt.plot(V1, V2)
plt.grid()
plt.xlabel('Input voltage $v_{i}$')
plt.ylabel('Output voltage $v_{o}$')
plt.savefig('p1vv.pdf')
plt.show()

plt.plot(I, V2)
plt.grid()
plt.xlabel('Output current $I_{o}$')
plt.ylabel('Output voltage $v_{o}$')
plt.savefig('p1iv.pdf')
plt.show()


V1 = []
V2 = []
I = []

with open('p2bad.data') as f:
    while True:
        raw = f.readline()
        if not raw: break
        dt = list(map(float, raw.split()))
        V1.append(dt[1])
        V2.append(dt[3])

plt.plot(V1, V2)
plt.grid()
plt.xlabel('Input voltage $v_{i}$')
plt.ylabel('Output voltage $v_{o}$')
plt.savefig('p2vvbad.pdf')
plt.show()

V1 = []
V2 = []
I = []

with open('p2.data') as f:
    while True:
        raw = f.readline()
        if not raw: break
        dt = list(map(float, raw.split()))
        V1.append(dt[1])
        V2.append(dt[3])
        I.append(dt[5])

plt.plot(V1, V2)
plt.grid()
plt.xlabel('Input voltage $v_{i}$')
plt.ylabel('Output voltage $v_{o}$')
plt.savefig('p2vv.pdf')
plt.show()

plt.plot(I, V2)
plt.grid()
plt.xlabel('Output current $I_{o}$')
plt.ylabel('Output voltage $v_{o}$')
plt.savefig('p2iv.pdf')
plt.show()


