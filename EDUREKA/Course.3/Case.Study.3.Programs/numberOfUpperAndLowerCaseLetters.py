'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
print("!! Program to calculate the number of upper case letters and lower case letters !!")
input_string = input("Enter the Input String : ")
upper_case = 0
lower_case = 0
for cal_val in input_string:
      if (cal_val.isupper()):
            upper_case=upper_case + 1
      elif (cal_val.islower()):
            lower_case=lower_case + 1
print("The number of uppercase characters is : ", upper_case)
print("The number of lowercase characters is : ", lower_case)
