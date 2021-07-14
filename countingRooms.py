import sys

sys.setrecursionlimit(10000000)

directions = [(0,1),(0,-1),(1,0),(-1,0)]

def dfs(gird,i,j):
    for a,b in directions:
        x,y = i+a,j+b
        if 0 <= x and x < n and 0 <= y and y < m and gird[x][y] == '.':
            gird[x][y] = "#"
            dfs(gird,x,y)


if __name__ == "__main__":
    n,m = map(int,input().split())
    gird = [list(input()) for i in range(n)]
    
    count = 0
    for i in range(n):
        for j in range(m):
            if gird[i][j] == '.': 
                gird[i][j] = '#'
                dfs(gird,i,j)
                count += 1

    print(count)            