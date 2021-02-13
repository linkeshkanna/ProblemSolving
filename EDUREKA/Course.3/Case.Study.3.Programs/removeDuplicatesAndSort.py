'''
Write a program that accepts a sequence of whitespace separated words 
as input and prints the words after removing all duplicate words and sorting them alphanumerically

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again

Then, the output should be:

again and hello makes perfect practice world
'''

import re
print("We are going to remove duplicates and sort them alphanumerically in a given String")
Inputstring = input()
if not re.match ( r'[a-zA-Z0-9 ]+$', Inputstring ): 
 print ("Enter AlphaNumeric Data only & Rerun the program!s")
else:
 words = Inputstring.split()
 Final = " ".join ( sorted ( set ( words ) , key=str.casefold ) )
 print("Result for unique and sort ascending data : ") 
 print(Final)



