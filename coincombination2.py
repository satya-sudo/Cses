md = 10**9 +7

n,m = map(int,input().split())
dp = [0 for i in range(m+1)]
dp[0] = 1
s = [int(x) for x in input().split()]
for i in s:
    j = 0
    while(j+i<=m):
        dp[j+i]+= dp[j]
        dp[i+j]%=md
        j+=1
print(dp[m])            