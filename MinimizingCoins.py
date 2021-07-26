dp = [0]*(10**6 +1)
import math
def finder(n):
    if  n == 0:
        return dp[n]
    for i in range(1,n+1):
        y = math.inf
        for j in ls:
            if i >= j:
                y = min(y,dp[i-j])
            else:
                break    
        dp[i] = y + 1
    return dp[n]   

if __name__ == "__main__":
    n,x  = map(int,input().split())
    ls = list(map(int,input().split()))
    ls.sort()
    x = finder(x)
    print(x) if x != math.inf else print(-1) 