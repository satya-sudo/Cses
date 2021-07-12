def sumFinder(n):
    return n*(n+1)/2 

if __name__ == '__main__':
    n  = int(input())
    s  =  sumFinder(n)
    setA = { i for i in range(1,n+1)}
    setB  = set()
    if s%2== 0:
        x = s/2
        while (x > n):
            setB.add(int(n))
            x -= n
            n -= 1
        setB.add(int(x))
        print("YES")
        print(len(setB))
        print(*setB)
        print(len(setA-setB))
        print(*setA-setB)
    else:
        print("NO")    


    