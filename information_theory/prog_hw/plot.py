import numpy as np
import matplotlib.pyplot as plt


py, pyerr = {}, {}

for fn in ['61.txt', '62.txt', '63.txt']:
    with open(fn) as f:
        for line in f:
            k, a, b = line.split()
            k = int(k)
            a = float(a)
            b = float(b)
            py[k] = a
            pyerr[k] = b

x = list(range(1, 65536+1))
y = [py[i] for i in x]
yerr = [pyerr[i] for i in x]

with open('65536.csv', 'w') as fw:
    for i, x in enumerate(y):
        fw.write('65536,%d,%.6f\n' % (i, x))
