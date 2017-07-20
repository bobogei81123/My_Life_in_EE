import numpy as np
import matplotlib.pyplot as plt

with open('d10000.data') as f:
    lines = f.readlines()

    xs = []
    ys = []

    for i, line in enumerate(lines):
        raw_data = [float(t) for t in line.split()]

        xs.append(raw_data[1])
        ys.append(raw_data[3])

    plt.plot(xs, ys)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.savefig('p10000.pdf')
    plt.show()
