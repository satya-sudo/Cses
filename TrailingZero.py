# no. of zero increases by 1 for every multiple of 5
# in cases of range <100 of 25 value  increases by 2
# in case of range <1000 prev value  +  125 value increase  by 2
# ... 



# https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/

import math
if __name__ ==  "__main__":
    n  =   int(input())
    x = 0
    while n >=  5:
        x +=  n//5
        n = n/5

    
    print(int(x))