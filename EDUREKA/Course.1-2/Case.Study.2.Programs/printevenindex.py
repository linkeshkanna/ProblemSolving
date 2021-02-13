myinput=list(input("Enter a String : " ))

word = ""
for x in myinput:
    if (myinput.index(x) % 2 == 0):
        word += x
print(word)
        

