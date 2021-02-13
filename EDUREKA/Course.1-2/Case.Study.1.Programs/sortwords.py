no_of_inputs = input("Please Enter no_of_inputs : ")

arr = list()
for i in range(int(no_of_inputs)):
    words = input('Enter the word : ')
    arr.append(words)

arr.sort()

for j in arr:
    print(j)
    
