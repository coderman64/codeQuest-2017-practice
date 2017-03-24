from __future__ import print_function

f = open('Prob04.in.txt', 'r')
numTests = int(f.readline())

for i in xrange(0, numTests):
    orgLine = (f.readline()).translate(None, '\n')
    words = orgLine.split('|')
    anagram = False
    ##print(words)       
    for letter in words[0]:
        ##print(letter)
        if letter not in words[1]:
            anagram = False
            break
        else:
            anagram= True
    if anagram:
        print(orgLine,'= ANAGRAM')
    else:
        print(orgLine,'= NOT AN ANAGRAM')
f.close()