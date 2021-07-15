from collections  import  defaultdict
from collections import deque

def bfs(i,d,visited):
    q = deque()
    q.append(i)
    while q:
        x = q.popleft()
        for j in d[x]:
            if visited[j] == False:
                visited[j] = True
                q.append(j)





if __name__ == '__main__':
    n,m = map(int,input().split())
    d = defaultdict(list)
    for i in range(m):
        a,b = map(int,input().split())
        d[a].append(b)
        d[b].append(a)
    visited = [False]*(n+1)
    lis = []
    for i in range(1,n+1):
        if visited[i] == False:
            visited[i] = True
            bfs(i,d,visited)
            lis.append(i)
    s = len(lis)
    print(s-1)        
    for i in range(s-1):
        print(lis[i],lis[i+1])


