
if __name__ == "__main__":
    n,m = map(int,input().split())
    s = list(map(int,input().split()))
    md = 10**9 +7
    dp = [1] + [0]*m
    dp[0] = 1
    for i in range(0,m+1):
        for j in s:
            if i + j <= m:
                dp[i+j] = (dp[i+j] +dp[i]) %md
           

    print(dp[m])