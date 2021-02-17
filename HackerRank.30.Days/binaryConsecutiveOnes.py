
    
if __name__ == '__main__':
    n = bin(int(input()))
    n = n[2:]
    print (max(map(len, n.split('0'))))
    