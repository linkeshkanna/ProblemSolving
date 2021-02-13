class divisibleBySeven:

    global start
    global end

    def __init__(object):
        object.start = 2000
        object.end = 3200

    def divisibleCheck(object):
        i = 2000
        list1 = []
        while i <= 3200:
            if(i%7 == 0):
                if(i%5 != 0):
                    list1.append(i)
            i += 1
        print(list1)

if __name__ == "__main__":
    object = divisibleBySeven()
    object.divisibleCheck()