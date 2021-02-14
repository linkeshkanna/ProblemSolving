if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    # print(arr)
    # print(len(arr))
    output = ""
    '''for i in range(len(arr) - 1, -1, -1):
        print(i)
        output.append(arr[i])
    print(output)'''
    for i in reversed(arr):
        output = output + str(i) + " " 
    print(output.rstrip())
