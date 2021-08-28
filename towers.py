from bisect import bisect_right
n = int(input())
lx = list(map(int,input().split()))
l = []
a = 0
for i in lx:
    p = bisect_right(l,i)
    if  p >= a:
        a += 1
        l.append(i)
        continue
    l[p] = i
print(a)