n = int(input())
tasks = []
for i in range(n):
    tasks.append(list(map(int,input().split())))

tasks.sort(key=lambda x: x[0])

ans = tasks[0][1] - tasks[0][0]
t = tasks[0][0]
for i in range(1,n):
    t += tasks[i][0]
    ans += tasks[i][1] -t
print(ans)     
