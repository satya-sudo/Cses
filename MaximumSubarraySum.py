import  math
if __name__ == '__main__':
    n = int(input())
    lis  =  list(map(int,input().split()))
    best  =  -math.inf
    sm = -math.inf
    for i in range(0, len(lis)):
        sm = max(lis[i],sm+lis[i])
        best = max(best,sm)
    print(best)    