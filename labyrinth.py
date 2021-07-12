import  math
def direction(x):
    return [[x[0],x[1]+1,"R",[]],[x[0],x[1]-1,"L",[]],[x[0]+1,x[1],"D",[]],[x[0]-1,x[1],"U",[]]]



def bfs(map,A):
    best  = math.inf
    res = None
    curRes = []
    q = []
    q.append(A)
    map[A[0]][A[1]] = 1
    while q:
        
        x = q.pop()
        
        x[3].append(x[2])
        
        for i in direction(x):
            if map[i[0]][i[1]] == "B":
                x[3].append(i[2])
                if len(x[3]) < best:
                    res = x[3]
                break
            if map[i[0]][i[1]] == ".":
                map[i[0]][i[1]] = "1"
                i[3] = x[3][0:]
                q.append(i)

    return res


if __name__ == '__main__':
    n , m = map(int,input().split())
    map = []
    A = 0
    for i in range(n):
        l = list(input())
        for j in range(m):
            if l[j] == "A":
                A = (i,j,"S",[])
        map.append(l)
    res = bfs(map,A)
    if   res != None:
        print("YES")
        print(len(res)-1)
        print("".join(res[1:]))    
    else:
        print("NO")
        


