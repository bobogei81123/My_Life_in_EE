import csv
import matplotlib.pyplot as plt
import numpy as np


with open('data/q2.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

    x = []
    y1 = []
    y2 = []
    y3 = []

for i in range(1, len(data)):
    x.append(data[i][0])
    y1.append(data[i][1])
    y2.append(data[i][2])
    y3.append(float(data[i][2]) - float(data[i][1]))


line1, = plt.plot(x, y1, lw=2, label=r'V_diode')
line2, = plt.plot(x, y2, lw=2, label=r'V_source')
line3, = plt.plot(x, y3, lw=2, label=r'V_resistor')
plt.legend(handles=[line1, line2, line3], loc=2)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('Source Voltage (V)')
plt.ylabel('Voltage (V)')

plt.savefig('data/q2i.pdf')
plt.show()



