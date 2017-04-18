
inputFile = open("Prob13.in.txt")
testCases = int(inputFile.readline())

def uniqueVals(li):
    newList = []
    for i in li:
        if not i in newList: 
            newList += [i]
    return newList

for i in range(testCases):
    totalNum = int(inputFile.readline().strip("FIND SUM=\n"))
    values = inputFile.readline().split(",")
    for i in range(len(values)):
        values[i] = int(values[i])
    values = sorted(values)
    done = False
    finalValues = [0]
    allCombinations = []
    while not done:
        rangeDone = True
        for i in range(len(finalValues)):
            if finalValues[i] != len(values)-1:
                rangeDone = False
        if rangeDone:
            #print(finalValues[len(finalValues)-1])
            if len(finalValues) < len(values):
                finalValues[len(finalValues)-1] = 0
                finalValues += [0]
            else:
                done = True
        finalValues[0] += 1;
        for i in range(1,len(finalValues)):
            if finalValues[i-1] == len(values):
                finalValues[i] += 1
                finalValues[i-1] = 0
        if uniqueVals(finalValues) == finalValues:
            totalValue = 0
            individualValues = ""
            for i in range(len(finalValues)):
                totalValue += values[finalValues[i]]
                if i > 0:
                    individualValues = str(values[finalValues[i]])+"+"+individualValues
                else:
                    individualValues = str(values[finalValues[i]])
            if totalValue == totalNum:
                allCombinations += [individualValues]
            #print("thinking: "+individualValues)
    allCombinations = uniqueVals(sorted(allCombinations))
    for i in allCombinations:
        print(i)
