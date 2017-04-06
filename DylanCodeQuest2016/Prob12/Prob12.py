
P3_CODE = int('1011',2)
def longDiv(data):
    """input a string with 1's and 0's representing binary"""
    data = int(data,2)
    done = False
    while not done:
        shifted_code = P3_CODE << data.bit_length()-P3_CODE.bit_length()
        data = data ^ shifted_code
        if data < int('1000',2):
            done = True
    return data

inputFile = open("Prob12.in.txt")
testCases = int(inputFile.readline())
for i in range(testCases):
    message = inputFile.readline()
    divResult = longDiv(message)
    if divResult == 0:
        print("ok")
    else:
        print("corrupt")
