md = 10**9 +7
n,m = map(int,input().split())
l = list(map(int,input().split()))
dp = [0]*(m+1)
if l[0] == 0:
    for i in range(1,m+1): dp[i] = 1
else:
    dp[l[0]] = 1

for i in range(2,n+1):
    nDp  = [0] * (m+1)
    if l[i-1] == 0:
        for j in range(1,m+1):
            if j-1 > 0:
                nDp[j] += dp[j-1]
            if j+1 <= m:
               nDp[j] += dp[j+1]
            nDp[j] += dp[j]
            nDp[j] = nDp[j]%md
    else:
        j = l[i-1]
        if j-1 > 0:
            nDp[j] += dp[j-1]
        if j+1 <= m:
           nDp[j] += dp[j+1]
        nDp[j] += dp[j]       
        nDp[j] = nDp[j]%md
    dp = nDp
    
ans = 0
for i in range(1,m+1):
    ans += dp[i]
print(ans% md)