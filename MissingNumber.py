if __name__ == '__main__' :
    n = int(input())
    sm = n*(n+1)//2
    lis =  sum(list(map(int,input().split())))
    print(int(sm - lis))