import numpy as np
import matplotlib.pyplot as plt

NUM = [1, 9, 25, 49]
LIMS = [(-8, 0.5), (-40, 40), (-60, 10), (-50, 40), (-40, 5)]

for num in NUM:
  with open('d' + str(num) + '.data') as f:
      lines = f.readlines()

      xs = []
      ys1 = []
      ys2 = []

      for i, line in enumerate(lines):
          raw_data = [float(t) for t in line.split()]

          xs.append(raw_data[0])
          ys1.append(raw_data[1])
          ys2.append(raw_data[3])

      plt.plot(xs, ys1)
      plt.plot(xs, ys2)
      plt.grid(True)
      #plt.ylim(LIMS[NUM-1])
      plt.ylim((-1.1, 1.1))
      if num == 1:
        plt.ylim((-1.4, 1.4))
      plt.xlim((0.150, 0.156))
      plt.legend(['$V_s$', '$V_o$'])
      plt.xlabel('time (s)')
      plt.ylabel('Voltage (V)')

      plt.savefig('p' +str(num) + '.pdf')
      plt.show()
