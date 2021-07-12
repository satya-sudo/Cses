# binary sreach approach total failure

# if __name__ == '__main__':
#     n,m = map(int,input().split())
#     st  = list(map(int,input().split()))
#     st.sort()
#     mx = len(st)
#     if mx %2 == 0:
#         mn = len(st)//2
#     else:
#         mn = len(st)//2 + 1
#     md  = (mx + mn)//2 
#     sm = sum(st)
#     while mn < mx:
#         md = (mx + mn)//2   
#         if (md*m > sm):
#             mn = md + 1
#         elif (md*n < sm):
#             mx = md -1
#         else:
#             print(md) 
#     print(md)    
# 
# #  frequecy technique not optimal   
# question is pretty straight forward       
# from collections  import  defaultdict

# if __name__ == '__main__':
#     n,m = map(int,input().split())
#     st  = list(map(int,input().split()))
#     d  = defaultdict(int)
#     for i in st:
#         d[i] += 1
#     count = 0
#     for j in st:
#         if (d[m-j] != 0 and d[j] != 0):  m-j + j maynot be the only option avaliable 
#             count += 1
#             d[j] -= 1
#             d[m-j] -= 1
#         elif (d[j] != 0):
#             count += 1
#             d[j] -= 1
#     print(count)   
# 
# 
#         
# two pointer approach
if __name__ == '__main__':
    n,m = map(int,input().split())
    st  = list(map(int,input().split()))
    st.sort()
    i = 0 
    j = len(st) - 1
    count = 0
    while(i <= j ):
        if (st[i]+st[j] == m):
            count+=1
            i += 1
            j -= 1
        elif  (st[i]+st[j] > m):
                count += 1
                j -= 1 
        else:
            count += 1
            i += 1
            j -= 1
    print(count)        

