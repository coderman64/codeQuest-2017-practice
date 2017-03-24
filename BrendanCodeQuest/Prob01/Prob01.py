import sys

def print_square(n):
    for rows in xrange(0, n):
        for length in xrange(0, n):
            sys.stdout.write('#')
            if length != n-1:
                sys.stdout.write(' ')
        print
        
f = open('Prob01.in.txt', 'r')
numTests = int(f.readline())
for tests in xrange(0, numTests):
    print_square(int(f.readline()))
    
f.close()