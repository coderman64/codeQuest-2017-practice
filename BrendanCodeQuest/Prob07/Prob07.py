from __future__ import print_function

f = open('Prob07in.txt', 'r')
numTests = int(f.readline())

for i in range(0, numTests): ## For each test case
    numLines = int(f.readline())
    normalPara = [None] *numLines## para array of lines
    print(numLines)
    for i in range(0, numLines): ## For each line, add to array
        normalPara[i] = (f.readline()).strip('\n')
        
    print(normalPara)
    coords = (f.readline()).strip('\n').split(',')
    coords[0] = int(coords[0])
    coords[1] = int(coords[1])
    print('Coordiantes: '+str(coords))
    
    numLinesSecret = int(f.readline())
    
    secretPara = ''
    for k in range(0, numLinesSecret):
        secretPara += (f.readline()).strip('\n')
    print(secretPara)##The secret paragraph changed form an array to one string, makes it easier
    
    startChar = (normalPara[coords[0]])[coords[1]]##Start char based on coordinates value
    secIndex = 0
    for i in range(coords[0],len(normalPara)):
        if i == coords[0]:
            print("Skip")
            for k in range(coords[1], len(normalPara[i])):
                
                if secIndex < len(secretPara) and secretPara[secIndex] == 'O':
                    print((normalPara[i])[k],end='')
                if secIndex < len(secretPara):
                    print(normalPara[i][k] + ' '+str(secIndex)+' '+secretPara[secIndex])
                secIndex += 1
        else:
            for letter in normalPara[i]:
                ##print(secIndex)
                if secIndex < len(secretPara) and secretPara[secIndex] == 'O':
                    print(letter,end='')
                if secIndex < len(secretPara):
                    print(letter + ' '+str(secIndex) +' '+secretPara[secIndex])
                secIndex += 1
            
    print('\nStart char: '+startChar)
f.close()
