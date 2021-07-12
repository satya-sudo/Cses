# binary search aproach  -> ok function will be too complicated 
if __name__ == '__main__':
    n = int(input())
    lis = list(map(int,input().split()))
    lis.sort()
    x = 1
    i = 0
    while (i < n and x >=lis[i]):
        x += lis[i]
        i += 1
    print(x)    

 