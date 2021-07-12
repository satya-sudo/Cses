from collections import defaultdict
if __name__ == '__main__':
    n , m = map(int,input().split())
    lis= list(map(int,input().split()))
    d = defaultdict(list)
    for i in range(len(lis)):
        d[lis[i]].append(i+1)
    flag =0    
    for i in lis:
        if i == m-i:
            if len(d[i]) >1:
                print(d[i][0],d[i][1])
                flag =1
                break
        elif len(d[m-i]) > 0:
            print(*d[i],*d[m-i])
            flag = 1
            break
    if flag == 0:
        print("IMPOSSIBLE") 