""" complicated """

import sys
I = sys.stdin.readline
n = int(I().strip())
l = []
for i in range(n):
    l.append(list(map(int,I().strip().split())))
l.sort(key=lambda x: x[1])
y = [x[1] for x in l] 
dp = [0]*(n)
dp[0] = l[0][2]

for i in range(1,n):
    
    lower = 0
    upper = i-1
    z = l[i][0]
    c  = -1
    while lower <=  upper:
        mid = (lower+upper)//2
        if y[mid] <  z:
            if y[mid+1] < z:
                lower = mid+1
            else:
                c = mid
                break
        else:
            upper = mid -1        
    temp = l[i][2]     
    if c != -1:        
        temp += dp[c]    
    dp[i] = max(dp[i-1],temp)
print(dp[n-1])