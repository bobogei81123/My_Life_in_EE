import numpy as np
import matplotlib.pyplot as plt


for i in range(1, 4):
  for j in range(1, 4):
    print('d'+str(i)+str(j))
    with open('d' + str(i) + str(j) + '.data') as f:
      lines = f.readlines()

      xs = []
      ys = []

      for z, line in enumerate(lines):
        raw_data = [float(t) for t in line.split()]

        xs.append(raw_data[0])
        ys.append(raw_data[1])

      plt.plot(xs, ys)
      plt.grid(True)
      plt.semilogx()
      plt.ylim((plt.ylim()[0], plt.ylim()[1]+0.5))
      plt.legend(['$V_O/V_I$'])
      plt.xlabel('frequency (Hz)')
      plt.ylabel('ratio (dB)')

      plt.savefig('p' +str(i)+str(j) + '.pdf')
      plt.show()
