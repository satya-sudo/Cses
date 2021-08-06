import math
n,m  = map(int,input().split())
dp = [[0 for i in range(m+1)] for j in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if i == j:
            dp[i][j] = 0
        else:
            md  = math.inf
            for d in range(1,i//2+1):
                md  = min(md,dp[d][j]+dp[i-d][j])
            for d in range(1,j//2+1):
                md = min(md,dp[i][d]+dp[i][j-d]) 
            dp[i][j] = 1 + md 
print(dp[n][m])               
