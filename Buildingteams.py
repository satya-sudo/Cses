"""
    We are using Two colors apppoach to solve this problem.
    First we are using dfs to find out the color of all the nodes.
    we any child node has the same color as thier parent then its a contradiction 
    and we return false.

    SO basically we are checking is the graph is a biparted or not 

"""



from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)


def dfs(x,teams,d,color):
    l = 2
    if color == 2:
        l = 1   
    for i in d[x]:
        if teams[i] == color:
            return False
        if teams[i] == 0:
            teams[i] = l
            if dfs(i,teams,d,l) == False:
                return False
            




if __name__ == "__main__":
    n,m = map(int,input().split())
    d = defaultdict(list)
    for i in range(m):
        a,b = map(int,input().split())
        d[a].append(b)
        d[b].append(a)
    teams = [0]*(n+1)
    for i in range(1,n+1):
        if teams[i] == 0:
            teams[i] = 1
            if dfs(i,teams,d,1) == False:
                print("IMPOSSIBLE")
                exit()
    for i in range(1,n+1):
        print(teams[i],end=" ")           
