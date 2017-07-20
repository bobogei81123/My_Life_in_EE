import matplotlib.pyplot as plt


t = []
x1 = []
x2 = []
x3 = []
x4 = []

with open('d3.data') as f:
    for ln in f:
        row = list(map(float, ln.split()))
        t.append(row[0])
        x1.append(row[1])
        x2.append(row[3])
        x3.append(row[5])
        x4.append(row[7])

#plt.xlim((0.0011, 0.0010))
plt.xlim((8e-3, 10e-3))
plt.xlabel('Time ($t$)')
plt.ylabel('Voltage ($V$)')
plt.plot(t, x1, linewidth=2, ls='-', color='black')
plt.plot(t, x2, linewidth=1)
plt.plot(t, x3, linewidth=1)
plt.plot(t, x4, linewidth=2)
plt.legend(['$V_S$', '$V_L$', '$V_R$', '$V_C$'])
plt.savefig('plt3.pdf')
plt.show()

