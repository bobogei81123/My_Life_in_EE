import csv
import matplotlib.pyplot as plt
import numpy as np


with open('data/q4.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

    x = []
    y1 = []

for i in range(1, len(data)):
    x.append(data[i][0])
    y1.append(data[i][1])


line1, = plt.plot(x, y1, lw=2, label=r'V_capacitor')
plt.legend(handles=[line1], loc=1)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('Source Voltage (V)')
plt.ylabel('Voltage (V)')
plt.xscale('log')

plt.savefig('data/q4i.pdf')
plt.show()



