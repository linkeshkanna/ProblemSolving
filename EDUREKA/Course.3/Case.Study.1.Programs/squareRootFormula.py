import math

class squareRoot:

    global C
    global H

    def __init__(object):
        object.C = 50
        object.H = 30

    def calculateSquareRoot(object, value):
        return math.sqrt((2 * object.C * value) / object.H)

if __name__ == "__main__":
    object = squareRoot()
    value = input("Enter Values in Comma Seperated Format : ")
    inputlist = value.split(',')
    resultlist = []
    for x in inputlist:
        resultlist.append(object.calculateSquareRoot(int(x)))
    print("Calculated SQRT for Entered Values are : ")
    results = list(map(int, resultlist))
    print(results)
