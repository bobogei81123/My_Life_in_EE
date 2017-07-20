import csv
import matplotlib.pyplot as plt
import numpy as np


with open('data/q3.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

    x = []
    y1 = []
    y2 = []

for i in range(1, len(data)):
    x.append(data[i][0])
    y1.append(data[i][1])
    y2.append(data[i][2])


line1, = plt.plot(x, y1, lw=2, label=r'V_capacitor')
line2, = plt.plot(x, y2, lw=2, label=r'V_source')
plt.legend(handles=[line1, line2], loc=2)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlim([0.005, 0.01])
plt.xlabel('Source Voltage (V)')
plt.ylabel('Voltage (V)')

plt.savefig('data/q3i.pdf')
plt.show()



