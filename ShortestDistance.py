from collections import defaultdict,deque
import math
import sys
sys.setrecursionlimit(1000000)
def dfs(graph,lis,s,visited):
    visited[s]=True
    for i in graph[s]:
        if not visited:
            dfs(graph,lis,i,visited)
    lis.append(s)        



if __name__ == "__main__":
    n,m = map(int,input().split())
    d = defaultdict(lambda:math.inf)
    graph = defaultdict(list)
    visited = [False]*(n+1)
    for i in range(m):    
        a,b,c = map(int,input().split())
        d[(a,b)] = min(d[(a,b)],c)
        graph[a].append(b)
        
    dis = [math.inf]*(n+1) 

    lis = []
    for i in range(1,n+1):
        if not visited[i]:
            dfs(graph,lis,i,visited)

    print(lis)
    dis[1] = 0
    for i in lis:
        for j in graph[i]:
            if dis[j] > dis[i] + d[(i,j)]:
                dis[j] = dis[i] + d[(i,j)]
    print(*dis[1:])            