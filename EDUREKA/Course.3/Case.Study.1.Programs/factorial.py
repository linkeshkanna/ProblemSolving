class factorial:

    def calculateFactorial(object, value1):
        value = int(value1)
        if value == 1:
            return value
        else:
            return value * object.calculateFactorial(value - 1)

if __name__ == "__main__":
    value = input("Please Enter a Number : ")
    object = factorial()
    fact = object.calculateFactorial(value)
    print("Factorial Of Number " + str(value) + " is : " + str(fact))
