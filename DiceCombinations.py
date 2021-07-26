dp = [0]*(10**6+1)
m = 10**9 + 7
def finder(n):
    if n == 0 or n == 1:
        return dp[n]
    for i in range(2,n+1):
        res = 0
        for j in range(0,7):
            if i > j:
                res = (res% m + dp[i-j]%m)%m 
        if i <= 6:
            res =  (res%m + 1)%m
        dp[i]  = res
    return dp[n]             


if __name__  == "__main__":
    n = int(input())
    dp[0] = 0
    dp[1] = 1
    print(finder(n))