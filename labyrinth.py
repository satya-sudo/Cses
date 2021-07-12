import sys

sys.setrecursionlimit(150000)



class Node:
    def __init__(self,coord =None,direction = None,parent =None):
        self.coord  = None
        self.direction =  None
        self.parent =  None
    def __str__(self) -> str:
        return f"(self.coord) and (self.direction)"    

def direction(x):
    m = Node()
    m.coord=(x[0],x[1]+1)
    m.direction="R"
    y = Node()
    y.coord=(x[0],x[1]-1)
    y.direction="L"
    z = Node()
    z.coord=(x[0]+1,x[1])
    z.direction="D"
    w = Node()
    w.coord=(x[0]-1,x[1])
    w.direction="U"
    return [m,y,z,w]



def dfsRec(A,visited,Map,res):
    visited.append(A.coord)
    
    for i in direction(A.coord):
        if Map[i.coord[0]][i.coord[1]] == "B":
            i.parent = A
            res.append(i)
            return

        if Map[i.coord[0]][i.coord[1]] == "." and i.coord not in visited:
            i.parent = A
            dfsRec(i,visited,Map,res)



if __name__ == "__main__":
    n , m = map(int,input().split())
    Map = []
    A = Node()
    Map.append(["#"]*(m+2))
    for i in range(n):
        l = ["#"] + list(input()) + ["#"]
        if not A.coord :
            for j in range(m+1):
                if l[j] == "A":
                    A.coord = (i+1,j) 
        Map.append(l)
    Map.append(["#"]*(m+2))
    visited = []
    res = []
    dfsRec(A,visited,Map,res)

    if len(res) == 0:
        print("NO")
    else:
        print("YES")
        s = []
        x = res[0]
        while  x != None  and x.direction != None:
            s.append(x.direction)
            x = x.parent
        l = "".join(s)
        print(len(l))            
        print(l[::-1])    
