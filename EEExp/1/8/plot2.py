
import matplotlib.pyplot as plt
from scipy import interpolate as intp
from scipy.optimize import bisect

X = [100, 200, 500, 1000, 2000, 5000, 1e4, 2e4, 5e4, 1e5, 2e5, 5e5, 1e6, 2e6]
A = [
  [ 104/104, None, 104/104, 104/104, None, 102/104, None, 102/102, 68/68, 100/100, 98/106, 64/92, 78/132, 54/100],
  [ 4.64e1, None, 46.4, 46.4, 46, 42.4, 2.96e3/80, 2.8e3/100, 1.3e1, 720/104, 560/100, 200/106, 68/106, 38/106],
  [ 4.64e1, None,  46.4, 46.4, 4.8e3/102, 4.32e3/102, 4.0e3/102, 2.72e3/98, 1.36e3/104, 720/104, 400/96, 200/102, 120/104, 120/104],
  [ 196/100, None, 196/100, 196/103, 200/102, 196/106, 200/102, 200/102, 204/100, 192/100, 168/100, 104/100, 60/102, 30/104],
  [ 104/98, None, 104/98, 102/98, None, 100/100, None, 104/102, 108/104, 104/102, 100/100, 104/102, 78/102, 50/100],
  ]


xs = []
ys = []

for i in range(len(A[1])):
  if A[1][i] != None:
    xs.append(X[i])
    ys.append(A[1][i])

f = intp.interp1d(xs, ys)
z = bisect(lambda x: f(x) - 1, 5e5, 1e6)
print(z)

plt.semilogx()
plt.plot(xs, ys, 'o-')
plt.scatter([z], [f(z)], marker='o', c='r', s=40.0)
plt.axhline(1, color='red')
plt.xlabel('frequency $f$ (log scale)')
plt.ylabel('Gain $A_v = V_o/V_i$')
plt.savefig('img/r1.pdf')
plt.show()


