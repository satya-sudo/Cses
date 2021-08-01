n = input()
c =  0
while(n != "0"):
    mx = 0
    for i in n:
        mx = max(mx,int(i))
    n =  f"{int(n) - mx}"
    c += 1
print(c)        