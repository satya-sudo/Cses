if __name__ ==  '__main__':
    n = int(input())
    arr  = list(map(int,input().split()))
    sm = 0 
    for  i in range(1,n):
        if arr[i] < arr[i-1]:
            
            sm += arr[i-1] - arr[i]
            arr[i] += arr[i-1] - arr[i] 
            
    print(sm)        
