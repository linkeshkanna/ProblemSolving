

if __name__ == '__main__':
    arr = []
    for i in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    hourGlass = []
    for i in range(0, len(arr) - 2):
        for j in range(0, len(arr) - 2):
            hourGlass.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + 
                  arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
    print(max(hourGlass))