from __future__ import print_function
import math

f = open('Prob05.in.txt', 'r')
numTests = int(f.readline())

for i in xrange(0, numTests):
    orgMoney = f.readline()
    total = float(orgMoney.translate(None, '$\n'))## remove any chars in delchar string
    print('Total of the bill: ' + orgMoney, end='')
    print('15% = $' + str(round(total * .15, 2))) ## round 2 decimals
    print('18% = $' + str(round(total * .18, 2)))
    print('20% = $' + str(round(total * .2, 2)))
    
f.close()