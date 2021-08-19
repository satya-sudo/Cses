for i in range(int(input())):
    n = int(input())
    c = 0
    l = 0
    while 1:
        c += 1
        if c % 3 == 0:
            continue
        if c%10  == 3:
            continue
        l += 1
        if l == n:
            print(c)
            break 