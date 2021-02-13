x = 1000
y = 3000

mylist = list()

while ( x <= 3000 ):
    string = str(x)
    evencondition = False
    for ch in string:
        if(int(ch) % 2 == 0):
            evencondition = True
            continue
        else:
            evencondition = False
            break
    if (evencondition):
        mylist.append(string + ',')
    x += 1

print(mylist)
