filename = 'c432.pat'
output = 'c432_p1'
with open(filename) as f, open(output, 'w') as fw:
    for l in f:
        wd = l.strip().split() 
        if not wd or wd[0] != 'force':
            continue

        pat = wd[2][1:-1]
        fw.write('{%s}\n' % pat)
