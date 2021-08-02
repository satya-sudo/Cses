"""
    its a 0-1 knapsack problem
    but the contains  n = 100 m =100000
    made it impossible to use the normal code  for python as 10**6 is the 1 sec mark for python
    had to make a few changes 1d dp
    and zip helps in python
"""



n,m = map(int,input().split())
W = list(map(int,input().split()))
V = list(map(int,input().split()))
dp = [0 for _ in range(m+1)]
for w,v in zip(W,V):
    for j in range(m,w-1,-1):
        dp[j] = max(dp[j],dp[j - w]+v) 
print(dp[m])               