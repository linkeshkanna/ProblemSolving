'''
Problem 1:

Write a program that accepts sequence of lines one by one in command line
as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:

Hello world
Practice makes perfect

Then, the output should be:

HELLO WORLD
PRACTICE MAKES PERFECT
'''

import re
print("We are going to convert words entered by user to UpperCase")
in_no_of_lines = input("Enter Number of Lines to Convert:")
if not in_no_of_lines.isdigit():
    print("Enter only number value for input line to begin!")
else:
    no_of_lines=int(in_no_of_lines)
    text = ""
    line_num_initiate = 0 
    while line_num_initiate < no_of_lines: 
        line = input()
        if not re.match(r'[A-Za-z ]+$', line):
            print("Only Alpha letters & Space are allowed.Rerun the Program to proceed Again!") 
            break
        line_num_initiate += 1
        text = text + "\n" + line.upper() 
    if not text.strip() == "":
         print("Converted String Result:") 
    print(text) 




