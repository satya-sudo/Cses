if __name__ ==  '__main__':
    n  = int(input())
    if (n !=  3 and n != 2):
        for i in range(n-1,0,-2):
            print(i,end=" ")
        for j in range(n,0,-2):
            print(j,end=" ")    
        print()
    else:
        print("NO SOLUTION")        