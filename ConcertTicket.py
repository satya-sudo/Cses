# two pointer approach   till now fail attempts  
# mutli set could be used as a hint 



if __name__ == '__main__':
    n ,m =  map(int,input().split())
    price  =  list(map(int,input().split()))
    price.sort()
    check  = [False] * len(price)
    bid = list(map(int,input().split()))
    i  =  0
    k = -1
    while(i < len(bid)):
        m  =  -1
        for j in range(0,len(price)):
            if (bid[i] < price[j]):
                break
            if( check[j] != True):
                k = j 
                m = price[j]
        if (k != -1):
            check[k-1] =  True
            k = -1    
        i += 1
        print(m)    