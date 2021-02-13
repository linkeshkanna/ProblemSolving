'''
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example:
0100,0011,1010,1001
Then the output should be:
1010, 0100

1000,1100,0100,0010 are divisible by 5
'''


print("")
print("!!Program which accepts a sequence of comma separated 4 digit binary numbers and they are divisible by 5 or not!!")
import re
print("")
input_string = input("Please enter list of 4 digit number made from 0 and 1 and Separted by Comma : ")
input_list = input_string.split(',')
iterate_list = iter(input_list)
element_lengnth = 4
if (all(len(len_var) == element_lengnth for len_var in iterate_list) and re.match(r'[01,]+$', input_string)):
    result_value = [div_vlue for div_vlue in input_list if not int(div_vlue) % 5]
    Result_UniqueSet=set(result_value)
    Result = ','.join([str(elem) for elem in result_value]) 
    Result_Unique = ','.join([str(elem) for elem in Result_UniqueSet])
    print("")
    print("Result of Given Numbers Divided by 5 : ", Result)
    print("")
    print("Result of Unique Number Divided by 5 : ", Result_Unique)
    print("")
else:
    print("")
    print("Please Enter Valid 4 digit number made from 0 and 1 and Separted by Comma to Reun Program! ")
    print("")