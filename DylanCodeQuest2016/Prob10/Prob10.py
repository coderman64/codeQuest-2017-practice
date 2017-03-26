
inputFile = open("Prob10.in.txt")
cases = int(inputFile.readline())

lastAlt = 0
lastEl = 0
alt = 0
el = 0
for i in range(cases):
    flightTime = int(inputFile.readline())
    for moment in range(flightTime):
        lastAlt = alt
        lastEl = el
        argList = inputFile.readline().split(",")
        alt = int(argList[0])
        el = int(argList[1])
        if alt*2-lastAlt <= el:
            print("PULL UP!")
        elif alt <= lastEl+500:
            print("Low Altitude!")
        else:
            print("ok")
        
