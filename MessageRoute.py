from collections import deque,defaultdict


def bfs(graph,visited,k,path,n):
    q = deque()
    q.append(k)
    path[k] = 0
    visited[k] = True
    while q:
        x = q.popleft()
        for i in graph[x]:
            
            if visited[i] ==  False:
                visited[i] = True
                path[i] = x
                q.append(i)
            if i == n:
                return (i)    

    return  -1

if __name__ == '__main__':
    n,m = map(int,input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False]*(n+1)
    path = [-1]*(n+1)
    res = bfs(graph,visited,1,path,n)
    if res == -1:
        print("IMPOSSIBLE")
    else:
        count = 0
        lis = []
        while res != 0:
            lis.append(res)
            count += 1
            res = path[res]
        print(count)
        print(*lis[::-1])    
