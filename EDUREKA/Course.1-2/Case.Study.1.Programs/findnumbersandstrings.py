s = input('Enter Some String : ')

numbers = sum(c.isdigit() for c in s)
words   = sum(c.isalpha() for c in s)

print("Numbers : " + str(numbers))
print("Alphabets : " + str(words))
