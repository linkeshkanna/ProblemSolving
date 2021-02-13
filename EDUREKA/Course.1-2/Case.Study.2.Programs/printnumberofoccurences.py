mystring = input("Enter a String : ")

uniquechars = ''.join(set(mystring))
print(uniquechars)

for x in uniquechars:
    print("Char : " + x + " - Count : " + str(mystring.count(x)))
