'''
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example:
0100,0011,1010,1001
Then the output should be:
1010
'''

''' BUG:
!!program which accepts a sequence of comma separated 4 digit binary numbers and they are divisible by 5 or not!!
Please enter list of 4 digit number made from 0 and 1 and Separted by Comma: 1010,0010,1000,0100,1001,1000
1010
'''

print("!!Program which accepts a sequence of comma separated 4 digit binary numbers and they are divisible by 5 or not!!")
import re
input_string = input("Please enter list of 4 digit number made from 0 and 1 and Separted by Comma : ")
input_list = input_string.split(',')
iterate_list = iter(input_list)
element_lengnth = 4
if (all(len(len_var) == element_lengnth for len_var in iterate_list) and re.match(r'[01,]+$', input_string)):
    result_value = [div_vlue for div_vlue in input_list if not int(div_vlue, 2) % 5]
    Result = ','.join([str(elem) for elem in result_value]) 
    print(Result)
else:
    print("Please Enter Valid 4 digit number made from 0 and 1 and Separted by Comma to Reun Program! ")