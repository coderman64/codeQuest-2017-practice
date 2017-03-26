# Prob11

alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(message,key):
    finalMessage = ""
    for char in message:
        index = alphabet.find(char.lower())
        if char == " ":
            finalMessage += " "
        elif char == char.lower():
            finalMessage += key[index].lower()
        else:
            finalMessage += key[index].upper()
    return finalMessage

def decrypt(message,key):
    finalMessage = ""
    for char in message:
        index = key.find(char.lower())
        if char == " ":
            finalMessage += " "
        elif char == char.lower():
            finalMessage += alphabet[index].lower()
        else:
            finalMessage += alphabet[index].upper()
    return finalMessage

inputFile = open("Prob11.in.txt")
cases = int(inputFile.readline())
for i in range(cases):
    function = inputFile.readline().strip("\n")
    key = inputFile.readline().strip("\n")
    mNum = int(inputFile.readline())
    for message in range(mNum):
        msg = inputFile.readline().strip("\n")
        if function == "ENCRYPT":
            print(encrypt(msg,key))
        else:
            print(decrypt(msg,key))
