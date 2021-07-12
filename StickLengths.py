import math
if __name__ == "__main__":
    n = int(input())
    lis = list(map(int,input().split()))
    lis.sort()
    x  = lis[n//2]
    c = 0
    for i in range(n//2):
        c += abs(x-lis[i])
        c += abs(x-lis[n-i-1])
    print(c)    