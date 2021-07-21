from collections import defaultdict as u;import math;import heapq as e
if __name__ == "__main__":
 n,m=map(int,input().split());d=u(list);v=[0]*(n+1)
 for i in range(m):    
  a,b,c=map(int,input().split());d[a].append((b,c))
 p=[math.inf]*(n+1);p[1]=0;h=[]
 e.heappush(h,(0,1))
 while h:
  s,r=e.heappop(h)
  if not v[r]:
   v[r]=1
   for i,y in d[r]:
    if p[i]>p[r]+y:
     p[i]=p[r]+y;e.heappush(h,(p[i],i))
 print(*p[1:])                


        