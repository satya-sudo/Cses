n = int(input())
grid = [input() for i in range(n)]
vist = [[ 0 for _ in range(n+1)] for _ in range(n+1)]
vist[0][1] = 1
md = 10**9 + 7
for i in range(1,n+1):
    for j in range(1,n+1):
        # print(i-1,j-1)
        # print(grid[i-1][j-1])

        if grid[i-1][j-1] == "*":
            vist[i][j] = 0
        else:
            vist[i][j] = (vist[i-1][j] + vist[i][j-1])% md
print(vist[n][n])
