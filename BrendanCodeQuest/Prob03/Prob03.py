from __future__ import print_function

f = open('Prob03.in.txt', 'r')
numTests = int(f.readline())

for i in xrange(0, numTests):
    lensTri = (f.readline()).translate(None, '\n').split(',')
    ##print(lensTri)
    for i in range(0, 3):
        lensTri[i] = int(lensTri[i])
        
    if (lensTri[0]+lensTri[1] > lensTri[2]) and (lensTri[1]+lensTri[2] > lensTri[0]) and (lensTri[0]+lensTri[2] > lensTri[1]):
        if lensTri[0] == lensTri[1] == lensTri[2]:
            print('Equilateral')
        elif lensTri[0] == lensTri[1] or lensTri[1] == lensTri[2] or lensTri[0] == lensTri[2]:
            print('Isoleces')
        else:
            print('Scalene')
    else:
        print('Not a Triangle')
        
f.close()