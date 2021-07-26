from heapq import*
I=lambda:map(int,input().split())
n,m=I()
G=[[]for _ in" "*n]
for _ in" "*m:
 a,b,w=I()
 G[a-1]+=(b-1,w),
D=[1e15]*n
Q=[(0,0)]
while Q:
 d,ss=heappop(Q)
 if d<D[ss]:
  D[ss]=d
  for e,g in G[ss]:heappush(Q,(d+g,e))
print(*D)