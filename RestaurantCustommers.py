
if __name__ == '__main__':
    d = []
    n = int(input())
    lis = []
    
    for i in range(n):
        x,y =  map(int,input().split())
        if x == 35484384:
            flag = 1
        lis.append((x,1))
        lis.append((y,-1))
     
    
    lis2 = sorted(lis,key=lambda  x:x[0])
    count = 0
    mx  = 0
    for i in lis2:
        count += i[1]
        mx = max(mx,count)
        
    print(mx)

