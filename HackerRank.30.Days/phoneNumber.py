
# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

if __name__ == '__main__':
    n = int(input())
    phoneNumbers = {}
    output = []
    for i in range(n):
        data = input().rstrip().split(' ')
        phoneNumbers[data[0]] = data[1]
    for i in range(n):
        data = input()
        if data in phoneNumbers.keys():
            output.append(str(data) + "=" + str(phoneNumbers[data]))
        else:
            output.append("Not found")
    print(*output, sep = "\n") 