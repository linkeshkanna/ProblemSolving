list1 = [12,24,35,70,88,120,155]

for x in list1:
    if(x%7 == 0):
        if(x%5 == 0):
            list1.remove(x)

print(list1)
