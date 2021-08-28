import sys
I = sys.stdin.readline
n = int(I())
l =  list(map(int,I().strip().split()))
ans = 0
s = set()
j = 0
for i in l:
    while i  in s:
        s.remove(l[j]) 
        j += 1  
    s.add(i)
    ans = max(ans,len(s))    
print(ans)