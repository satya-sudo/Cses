from collections import defaultdict
import math
import heapq
if __name__ == "__main__":
    n,m,q = map(int, input().split())
    lis = []
    graph  = defaultdict(list)
    for _ in range(m):
        a,b,c = map(int, input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))

    queres  = []

    for _ in range(q):
        f,g = map(int,input().split())
        # queres.append((a,b))
        d = [math.inf]*(n+1)   
        d[f] = 0
        vis = [0]*(n+1)
        q =[]
        heapq.heappush(q,(0,f))
        while q:
            p,u = heapq.heappop(q)
            if u  == g:
                queres.append(p)
                break
            if not vis[u]:
                vis[u] =  1
                for Node,dis in graph[u]:
                    if d[Node] >  d[u] + dis:
                        d[Node] = d[u] + dis
                        
                        heapq.heappush(q,(d[Node],Node))
        if d[f]  == math.inf or d[g] == math.inf:
            queres.append(-1)
            continue
                    
    [print(i) for i in queres]
