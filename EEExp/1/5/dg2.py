
with open('dt2.csv', 'w') as f:
    f.write('r,ext,trt,er\n')
    rdata = [(4.95, 10, 2.12), (4.01, 10, 2.61), (2.97, 10, 3.08), (1.99, 10, 5.15)]
    for dt in rdata:
        r = dt[0]
        l = dt[1]
        tau = l / r
        er = (dt[2] - tau) / tau

        f.write('{:.2f},{:.2f},{:.2f},{:.1f}\n'.format(r, dt[2], tau, er*100))

