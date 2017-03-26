#Navigating the world - prob 09 - codequest 2016 practice
import math

def getX(long, zoom):
    """get the x-coordinate based off of the given equation"""
    return math.floor((long+180)/360*(2**zoom))

def getY(lat, zoom):
    """get the y coorinate based off of the given equation"""
    return math.floor((1-(math.log(math.tan(lat*(math.pi/180))+1/math.cos(lat*(math.pi/180))))/math.pi)*2**(zoom-1))

inputFile = open("Prob09.in.txt")
cases = int(inputFile.readline())
for i in range(cases):
    caseValues = inputFile.readline().split(" ")
    zoomLevel = int(caseValues[0])
    lat = float(caseValues[1])
    long = float(caseValues[2])
    #replaces each %s in the url with the respective value in the tuple
    finalURL = "http://tile.openstreetmap.org/%s/%s/%s.png" % (str(zoomLevel),str(getX(long,zoomLevel)),str(getY(lat,zoomLevel)))
    print(finalURL)
