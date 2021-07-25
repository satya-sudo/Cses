"""
    we are using bellmenn ford 's algorithm to find the longest  path
    we are converting longest to shortest path by multiplying the weights by -1 
    we know bellmenn ford algo gives path in n-1 iterations but if values are changing 
    even after n-1 iteration this mean there is a +ve cycle 
    we just have to check if this cycle is part of the path from 1 to n
    if yes the path lenght will reach + infinty 
    else answer is the answer only 

"""


import sys
sys.setrecursionlimit(10**6)
import math
from collections import defaultdict

def dfs(g,v,s):
    v[s] = True
    for i in g[s]:
        if not v[i]:
            dfs(g,v,i)
if __name__  == "__main__":

    n,m = map(int,input().split())
    arr = []
    g1 = defaultdict(list)
    g2 = defaultdict(list)
    for i in range(m):
        a,b,c = map(int,input().split())
        g1[a].append(b)
        g2[b].append(a)
        arr.append((a,b,-c))
    d = [math.inf]*(n+1)
    d[1] = 0
    flag = 0
    vis1 =[False]*(n+1)
    vis2 =[False]*(n+1)

    dfs(g1,vis1,1)
    dfs(g2,vis2,n)
    for i in range(n):
        for s,t,r in arr:
            if d[t]> d[s] +r:
                d[t] = d[s] +r
                if i == n-1 and vis1[t] and vis2[t] :
                    flag = 1
                    print(-1)
                    exit()
    print(-1) if flag else print(-d[n])                