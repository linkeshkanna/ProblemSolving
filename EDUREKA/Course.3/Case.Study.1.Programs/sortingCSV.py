class sortCommaSeperatedValues:

    def sortCSV(self, value):
        myList = value.split(',')
        print("myList : ", myList)
        myList.sort()
        print("myList sorted : ", myList)
        return myList

if __name__ == "__main__":
    inputvalue = input("Please Enter Comma Seperated Strings to Sort : ")
    sortObject = sortCommaSeperatedValues()
    sortingString = sortObject.sortCSV(inputvalue)
    print("Sorted List", sortingString)
    print("Sorted Values in CSV : ", sortingString)


