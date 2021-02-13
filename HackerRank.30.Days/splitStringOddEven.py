# HackerRank
# https://www.hackerrank.com/challenges/30-review-loop/problem

if __name__ == '__main__':
    n = int(input())
    inputs = []
    for i in range(n):
        inputs.append(input())
    print(inputs)
    oddList, evenList = "", ""
    for i in range(n):
        print(i)
        print(inputs[i])
        counter = 1
        for j in inputs[i]:
            if counter % 2 == 0:
                evenList += j
            else:
                oddList += j
            counter += 1    
        print(evenList, oddList)
        oddList, evenList = "", ""

