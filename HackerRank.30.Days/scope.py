class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        differenceList = []
        print(self.__elements)
        for i in range(0, len(self.__elements) - 1):
            for j in range(0, len(self.__elements) - 1):
                differenceList.append(abs(self.__elements[i] - self.__elements[j+1]))
            print(differenceList)
        self.maximumDifference = max(differenceList)

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
