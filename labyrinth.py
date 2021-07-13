"""
    we are going to use bfs with rhombus radiation 
    the trick is we ll mark parent for each value 
"""
# node  -> pos
#       -> parent


from collections import deque 
drection = [(0,1),(0,-1),(1,0),(-1,0)]



def direction(b,x):
    for i in range(4):
        if (x[0]+drection[i][0],x[1]+drection[i][1]) == b:
            if i == 0:
                return "R"
            if i == 1:
                return "L"
            if i == 2:
                return "D"
            else:
                return "U"          



def isvalid(s):
    if 0 <= s[0]<n and 0<=s[1]<m and grid[s[0]][s[1]] != "#" and visited[s[0]][s[1]] == False:
        return True
    return False    



def bfs(s):
    q = deque()
    q.append(s)
    visited[s[0]][s[1]] = 1
    while q:
        x = q.popleft()
        for a,b in drection:
            if isvalid((x[0]+a,x[1]+b)):
                q.append((x[0]+a,x[1]+b))
                visited[x[0]+a][x[1]+b] = 1
                path[x[0]+a][x[1]+b] = x
                if grid[x[0]+a][x[1]+b]  == "B":
                    return (x[0]+a,x[1]+b)   
    return None

    
# input 

n,m = map(int,input().split())
grid = []
start =  None
visited =[]
for i in range(n):
    l = []
    for j in range(m):
        l.append(0)
    visited.append(l)    
path = [[None for i in range(m)] for j in range(n)]

for i in range(n):
    l = list(input())
    grid.append(l)
    if start == None:
        for j in range(m):
            if l[j] == 'A':
                start = (i,j)
    
    
b = bfs(start)
if b:
    res = []
    c = 0
    while b  != start:
        x = b
        b = path[b[0]][b[1]]
        res.append(direction(x,b))
        c += 1
    print("YES")
    print(c)
    print("".join(res)[::-1])    
else:
    print("NO")    









