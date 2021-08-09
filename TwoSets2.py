n = int(input())
s = n*(n+1) // 2
if s%2 != 0:
    print(0)
    exit()
s= s//2

dp = [1] + [0]*s
for i in range(1,n):
    # nDp = [1] + [0] * s
    for j in range(s,i-1,-1):
        dp[j] += dp[j-i]
        dp[j] %= 10**9+7
print(dp[s])