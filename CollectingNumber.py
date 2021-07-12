if __name__ == '__main__':
    n = int(input())
    lis = list(map(int,input().split()))
    lis1 = [0]*(n+1)
    for i in range(n):
        lis1[lis[i]] = i 
    count = 1
    for i in range(n):
        if lis1[i] >lis1[i+ 1]:
            count += 1 
         
    print(count)        