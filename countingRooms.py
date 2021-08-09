import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000000)

directions = [(0,1),(0,-1),(1,0),(-1,0)]

# def dfs(gird,i,j):
#     for a,b in directions:
#         x,y = i+a,j+b
#         if 0 <= x and x < n and 0 <= y and y < m and gird[x][y] == '.':
#             gird[x][y] = "#"
#             dfs(gird,x,y)


if __name__ == "__main__":
    n,m = map(int,input().strip().split())
    gird = [list(input().strip()) for i in range(n)]
    
    count = 0
    for i in range(n):
        for j in range(m):
            if gird[i][j] == '.': 

                # marking the visited points
                count += 1
                q = [(i,j)]
                while q:
                    z,v = q.pop()
                    for a,b in directions:
                        x,y = z+a,v+b
                        if 0 <= x and x < n and 0 <= y and y < m and gird[x][y] == '.':
                            gird[x][y] = "#"
                            q.append((x,y))



    print(count)            