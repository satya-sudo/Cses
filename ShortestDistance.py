from collections import defaultdict,deque
import math
import heapq as hq
import sys

""" 
    dijkstra shortest path
"""

if __name__ == "__main__":
    n,m = map(int,input().split())
    d = defaultdict(list)
    visited = [False]*(n+1)
    for i in range(m):    
        a,b,c = map(int,input().split())
        d[a].append((b,c))
       
        
    dis = [math.inf]*(n+1) 

    dis[1] = 0

    heap = []
    hq.heappush(heap,(0,1))
    while heap:
        x = hq.heappop(heap)
        if not visited[x[1]]:
            visited[x[1]] = True
            for i in d[x[1]]:
                if dis[i[0]] > dis[x[1]]+i[1]:
                    dis[i[0]] = dis[x[1]]+i[1]
                    hq.heappush(heap,(dis[i[0]],i[0]))
    print(*dis[1:])                


        