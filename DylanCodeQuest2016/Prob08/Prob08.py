from math import *
#Prob08 - code

#alphabet = "abcdefghijklmnopqrstuvwxyz "

inputFile = open("Prob08.in.txt")
cases = int(inputFile.readline())

for i in range(cases):
    songNumber = int(inputFile.readline())
    songList = {}
    for i in range(songNumber):
        songDesc = inputFile.readline().split(" - ")
        if songDesc[1].strip("\n") in songList:
            songList[songDesc[1].strip("\n")] += [songDesc[0]]
        else:
            songList[songDesc[1].strip("\n")] = [songDesc[0]]
    sortedKeys = sorted(iter(songList.keys()))
    for band in sortedKeys:
        for song in songList[band]:
            print(song+" - "+band)
