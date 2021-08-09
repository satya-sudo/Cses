import sys
I  = sys.stdin.readline
n = int(I())
a = list(map(int,I().split()))
s = sum(a)
dp = [True] + [False]*s
for i in range(1,n+1):
    nDp = [True] + [False]*s
    for j in range(1,s+1):
        if j >= a[i-1]:
            nDp[j] = dp[j] or dp[j-a[i-1]]
        else:
            nDp[j] = dp[j]
    dp = nDp
l = []    

for i in range(1,s+1):
    
    if dp[i]:
        l.append(i)

print(len(l))
print(*l)



