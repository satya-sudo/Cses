def calculator(n):
    x  =  n*n*(n*n-1)/2  # choicing 2 positions from n^2 positions 
    y = 4 * (n-2) * (n-1) # no of 2*3 or 3*2 boxs   -> each box will have 4 possible positions 
    return int(x - y)


if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(calculator(i))