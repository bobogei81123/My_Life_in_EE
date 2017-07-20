import math

raw_data = [(100, 3.6, 0.1), (200, 3.8, 0.2),
            (500, 3.6, 1.0),
            (1000, 3.2, 1.5),
            (2000, 2.4, 1.8),
            (5000, 1.6, 1.4),
            (10000, 0.7, 0.7),]

p_data = []
dname = ["col" + chr(ord('a') + i) for i in range(0, 6)]

for tup in raw_data:
    omg = tup[0] * 2 * math.pi
    trtht = math.atan2(omg * 0.0001, 1)
    extht = math.asin(tup[2]/tup[1])
    p_data.append([format(tup[0]) if tup[0] < 1000 else str(tup[0]//1000) + "\\si{\\kilo}"
       , format(tup[1]), format(tup[2]), format(extht*180/math.pi, '.3f')
       , format(trtht*180/math.pi, '.3f'), format((trtht - extht) / extht * 100.0, '.2f')
       ])

with open('tab1.csv', 'w') as f:
    f.write(','.join(dname))
    f.write('\n')
    for ln in p_data:
        f.write(','.join(map(str, ln)))
        f.write('\n')

raw_data2 = [(100, 2400),
             (140, 1160),
             (110, 400),
             (96, 168),
             (68, 62),
             (38, 12),
             (21, 3.2),]

for i in range(len(raw_data2)):
    raw_data2[i] = (raw_data[i][0],) + raw_data2[i]

p_data = []
dname = ["col" + chr(ord('a') + i) for i in range(0, 5)]
for tup in raw_data2:
    omg = tup[0] * 2 * math.pi
    trtht = math.atan2(omg * 0.0001, 1)
    extht = tup[1]/(1e6/tup[0]) * math.pi * 2
    p_data.append([
            format(tup[0]) if tup[0] < 1000 else str(tup[0]//1000) + "\\si{\\kilo}",
            format(tup[1]),
            format(tup[1]/(1e6/tup[0]) * 360, '.3f'),
            format(trtht * 180 / math.pi, '.3f'),
            format((extht - trtht) / trtht * 100, '.2f'),
            ])
with open('tab2.csv', 'w') as f:
    f.write(','.join(dname))
    f.write('\n')
    for ln in p_data:
        f.write(','.join(map(str, ln)))
        f.write('\n')

print(raw_data2)

