# naive apporoach 
# issue time limit exceeded
# assumption appartments array is sorted 

#  atemmpt 1
# if __name__ == '__main__':
#     n,m,p = map(int,input().split())
#     applications  = list(map(int,input().split()))
#     appartments = list(map(int,input().split()))
#     count = 0 
#     flag = -1
#     for i in range(0,len(applications)):
#         x,y =  applications[i]-p,applications[i]+p
#         for j in range(0,len(appartments)):
#             if (x <= appartments[j] and appartments[j] <= y):
#                 count += 1
#                 flag = j
#                 break
#         if flag != -1:
#             appartments.pop(flag)
#             flag = -1  

#     print(count)            

# attempt 2 sweeper version


if __name__ == '__main__':
    n,m,p = map(int,input().split())
    applications  = list(map(int,input().split()))
    appartments = list(map(int,input().split()))
    appartments.sort()
    applications.sort()
    i = 0
    j = 0
    count = 0
    while(i<len(applications) and j < len(appartments)):
        if (appartments[j] < applications[i] -p ):
            j += 1
        elif (appartments[j] > applications[i] +p ):
            i += 1
        else:
            count += 1
            j += 1
            i += 1
    print(count)            
