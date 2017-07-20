import matplotlib.pyplot as plt


t = []
x1 = []
x2 = []
x3 = []

with open('d1.data') as f:
    for ln in f:
        row = list(map(float, ln.split()))
        t.append(row[0])
        x1.append(row[1])
        x2.append(row[3])
        x3.append(row[5])

#plt.xlim((0.0011, 0.0010))
plt.xlim((1, 1.01))
plt.xlabel('Time ($t$)')
plt.ylabel('Voltage ($V$)')
plt.plot(t, x1)
plt.plot(t, x2)
plt.plot(t, x3)
plt.legend(['$V_S$', '$V_R$', '$V_C$'])
plt.savefig('plt1.pdf')
plt.show()

