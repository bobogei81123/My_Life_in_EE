
with open('dt1.csv', 'w') as f:
    f.write('r,ext,trt,er\n')
    rdata = [(9.95, 110, 740), (7.52, 110, 704), (5.04, 110, 460), (3.24, 110, 330)]
    for dt in rdata:
        r = dt[0]
        c = dt[1]
        tau = r * c
        er = (dt[2] - tau) / tau

        f.write('{:.2f},{:.2f},{:.2f},{:.1f}\n'.format(r, dt[2], tau, er*100))

