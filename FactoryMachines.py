n,m  = map(int,input().split())
l  = list(map(int,input().split()))
import math
# BINARY SEARCH

low  = 0
high = 10**18
ans = math.inf
while low <= high:
    mid  = (low+high)//2
    prod = 0
    for i in l:
        prod += mid//i
    if prod >= m:
        ans = min(ans,mid)
        high = mid-1
    else:
        low = mid+1

print(ans)        