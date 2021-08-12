"""
    lists can be faster than dict
    almost same approach as collecting Number 1

"""

import sys
I = sys.stdin.readline
n,m  =  map(int,I().strip().split())
l = list(map(int,I().strip().split()))
d = [0]*(n+1)
d2= [0]*(n+1)

for i in range(n):
    d[l[i]] = i+1
    d2[i+1] = l[i] 
count = 1

for i in range(n-1):
    if d[i+1] > d[i+2]:
        count += 1
for j in range(m):
    a,b = sorted(map(int,I().strip().split()))
    if a==b:
        print(count)
        continue
    x,y  = d2[a],d2[b]
    s = set()
    if 1 < x:
        s.add((x-1,x))
    if x < n:    
        s.add((x,x+1))
    if 1 < y:
        s.add((y-1,y))
    if y <n:    
        s.add((y,y+1))

    for x,y in s:
        if d[x] > d[y]:
            count -= 1

    d[d2[a]] = b
    d[d2[b]] = a
    d2[a],d2[b] = d2[b],d2[a]
    for x,y in s:
        if d[x] > d[y]:
            count += 1
    print(count)        
    
