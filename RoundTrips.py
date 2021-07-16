"""
    detection of cycle in a graph (undirected)
    input: adjacency list of the graph
    output: path of the cycle
    
    use DFS to detect a cycle in the graph.
    if a cycle is found, return the path of the cycle.

    bfs could be used but i had some trouble with it.
    so i switch to DFS

"""


from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

def Dfs(adj,path,start,parent,visited):
    visited[start] = True
    path[start] = parent
    for v in adj[start]:
        if visited[v] == False:
            x = Dfs(adj,path,v,start,visited)
            if x !=  None:
                return x
        elif visited[v] == True and parent != v:
            return (v,start)
    return None  
            

if __name__ == "__main__":
    n,m = map(int,input().split())
    adj = defaultdict(list)
    for _ in range(m):
        a,b = map(int,input().split())
        adj[a].append(b)
        adj[b].append(a)
    path  = [0]*(n+1)
    visited = [False]*(n+1)
    res = None
    for i in range(1,n+1):
        if visited[i] == False:
            res = Dfs(adj,path,i,-1,visited)
            if res != None:
                a,b = res
                ls = []
                while(a != b):
                    ls.append(b)
                    b = path[b]
                ls = [a] +ls +[a]
                print(len(ls))
                print(*ls)
                exit()
    print("IMPOSSIBLE")            


