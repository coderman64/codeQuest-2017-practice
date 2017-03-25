# Prob07 - the 7th problem of Code Quest 2016

inputFile = open("Prob07.in.txt")
testCases = int(inputFile.readline())

for i in range(testCases):
    #make the message into a list of strings
    messageLength = int(inputFile.readline()) #read the line with the message length
    message = []
    for i in range(messageLength):
        message.append(inputFile.readline().strip("\n"))
    #make the messageX and messageY are the coordinates for the cover message
    messageY, messageX = inputFile.readline().strip("\n").split(",")
    messageX = int(messageX)
    messageY = int(messageY)
    #make the cover into a list of strings
    coverLength = int(inputFile.readline().strip("\n"))
    cover = []
    for i in range(coverLength):
        cover.append(inputFile.readline().strip("\n"))

    finalMessage = ""
    for line in range(coverLength):
        for letter in range(len(cover[line])):
            if cover[line][letter] == "O":
                finalMessage += message[line+messageY][letter+messageX];
    print(finalMessage)
