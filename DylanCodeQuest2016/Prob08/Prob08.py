from math import *
#Prob08 - code

alphabet = "abcdefghijklmnopqrstuvwxyz"

class song:
    def __init__(self,title,artist):
        self.title = title.strip(" ")
        self.artist = artist.strip(" ")

def sortSongTitle(listArtist):
    newList = [listArtist[0]]
    for i in range(1,len(listArtist)):
        done = False
        x = 0
        while not done:
            if x>=len(newList):
                listArtist.append(listArtist[i])
                done = True
            elif alphabet.find(listArtist[i].title)<newList[x]:
                listArtist.insert(x,listArtist[i])
                done = True
            x += 1
    return newList

def sort(songList):  
    lists = {}
    for i in songList:
        if i.artist not in lists.keys:
            lists[i.artist] = [i]
        else:
            lists[i.artist].append(i)
    
    for i in iter(lists.keys()):
        
    
inputFile = open("Prob08.in.txt")
cases = int(inputFile.readline())
for i in range(cases):
    songNumber = int(inputFile.readline())
    songList = []
    for i in range(songNumber):
        songDesc = inputFile.readline().split(" - ")
        songList.append(song(songDesc[0],songDesc[1].strip("\n")))
    for i in songList:
        print(i.title+" - "+i.artist)
