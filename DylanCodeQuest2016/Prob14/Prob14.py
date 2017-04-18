
inputFile = open("Prob14.in.txt")
testCases = int(inputFile.readline())
for case in range(testCases):
    game = inputFile.readline().split(",")
    frameScores = []
    
    #score the first nine frames
    for i in range(9):
        if game[i] == "X":
            frameScores.append([10,"X"])
        elif game[i].endswith("/"):
            frameScores.append([10,"/"])
        else:
            thisScore = 0
            for char in game[i]:
                if char != "-":
                    thisScore += int(char)
            frameScores.append([thisScore,"N"])
        #add scores to previous strikes and spares
        if i >= 2 and frameScores[i-2][1] == "X":
            frameScores[i-2][0] += frameScores[i][0];
        if i >= 1 and (frameScores[i-1][1] == "X" or frameScores[i-1][1] == "/"):
            frameScores[i-1][0] += frameScores[i][0]

    #score frame 10
    frameScore = 0
    if len(game[9]) < 3:
        for i in game[9]:
            frameScore += int(i)
    else:
        for i in game[9]:
            if i == "X"
    finalScore = 0
    for i in frameScores:
        finalScore += i[0]
    print(finalScore)
