# o(n^2)
# import sys
# I =  sys.stdin.readline
# n = int(I().strip())
# dp = [1 for i in range(0,n+1)]
# l = [int(i) for i in I().strip().split()]
# ls = 1
# for i in range(0,n):
#     for j in range(i+1,n):
#         if l[i] < l[j]:
#             dp[j] = max(dp[j],1+dp[i])
#             ls = max(ls,dp[j])

# print(ls)        


# o(nlogn)
import sys
I =  sys.stdin.readline
n = int(I().strip())
dp = []
l = [int(i) for i in I().strip().split()]
dp.append(l[0])
for i in range(1,n):
    x = 0
    y = len(dp)
    while x < y:
        m = (x+y)//2
        if dp[m] < l[i]:
            x = m+1
        else:
            y = m
    if x == len(dp):
        dp.append(l[i])
    else:
        dp[x] = l[i]    


print(len(dp))        