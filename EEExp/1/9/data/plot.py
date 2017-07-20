
import matplotlib.pyplot as plt

X = [1e3, 2e3, 5e3, 1e4, 2e4, 5e4, 1e5, 2e5]
Xs = [1e3, 2e3, 5e3, 1e4, 2e4, 2.5e4, 3e4, 5e4, 1e5, 2e5]
A = [
  [ 340/400, 332/400, 316/408, 268/416, 168/424, 47.6/448, 15.6/448, 6.8/448],
  [372/392, 384/408, 400/408, 480/400, 496/392, 304/408, 192/416, 68/408, 15.6/416, 5.8/416],
  [8.4/728, 14.4/736, 72/744, 176/744, 384/720, 592/660, 640/676, 656/672],
  [53.6/472, 146/696, 314/688, 488/680, 592/680, 636/680, 644/672, 648/664],
  [136/728, 192/744, 380/760, 568/776, 748/800, 480/752, 264/720, 133/720],
  [42.0/760, 58.4/792, 128/784, 304/784, 700/792, 240/768, 88.0/768, 39.2/768
  ]
]

for i in range(len(A)):
  xs = []
  ys = []
  dt = A[i]
  print(len(dt))
  for j in range(len(dt)):
    if dt[j] != None:
      if i == 1:
        xs.append(Xs[j])
      else:
        xs.append(X[j])
      ys.append(dt[j])

  plt.plot(xs, ys, 'o-')
  plt.semilogx()
  plt.semilogy()
  plt.ylim((0, plt.ylim()[1]))
  plt.xlabel('frequency $f$ (log scale)')
  plt.ylabel('Gain(db) $\log (V_o/V_i)$')
  plt.savefig('img/q' + str(i+1) + '.pdf')
  plt.show()
  


