
# Complete the factorial function below.
# https://www.hackerrank.com/challenges/30-recursion/problem
def factorial(n):
    if n == 1:
        return n
    else:
        return(n * factorial(n - 1))

if __name__ == '__main__':
    n = int(input())
    result = factorial(n)
    print(result)
    
