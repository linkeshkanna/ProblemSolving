class twodArray:

    def generateArray(self, X, Y):
        Matrix = [[0 for i in range(X)] for j in range(Y)]
        k = 0
        l = 0
        print(Matrix)
        while k < Y:
            l = 0
            while l < X:
                Matrix[k][l] = k * l
                l += 1
            k += 1
        print(Matrix)

if __name__ == "__main__":
    inputvalue = input("Please Enter two comma separated Values to Create 2D Array : ")
    list1 = inputvalue.split(',')
    x = int(list1[0])
    y = int(list1[1])
    object = twodArray()
    object.generateArray(x, y)
