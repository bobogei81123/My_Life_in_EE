import numpy as np
import matplotlib.pyplot as plt

NUM = 6
LIMS = [(-8, 0.5), (-40, 40), (-60, 10), (-50, 40), (-40, 5)]

with open('d' + str(NUM) + '.data') as f:
    lines = f.readlines()

    xs = []
    ys = []

    for i, line in enumerate(lines):
        raw_data = [float(t) for t in line.split()]

        xs.append(raw_data[0])
        ys.append(raw_data[1])

    plt.plot(xs, ys)
    plt.grid(True)
    plt.semilogx()
    plt.ylim(LIMS[NUM-1])
    plt.legend(['$V_O/V_I$'])
    plt.xlabel('frequency (Hz)')
    plt.ylabel('ratio (dB)')

    plt.savefig('p' +str(NUM) + '.pdf')
    plt.show()
