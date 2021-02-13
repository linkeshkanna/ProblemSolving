mynumber = int(input("Enter an Number : "))

no = mynumber
sum=0

while(no >= 1):
    sum = (sum + (no/(no+1)))
    no -= 1;
print(sum)
