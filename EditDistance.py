import sys

"""
    base case :
        n == 0:
        return m
        m == 0:
        return n 
    choice diagram :
        i-1,j --> removed
        i,j-1 --> added
        i-1,j-1 --> replaced

    opinion :
        this question busted my brain 
        the thinking of  base case made a hole in my brain

"""

I = sys.stdin.readline
s1 = I().strip()
s2 = I().strip()
dp = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
for i in range(1,len(s2)+1): dp[0][i] = i
for i in range(1,len(s1)+1): dp[i][0] = i
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s2[j-1] == s1[i-1]:
            dp[i][j] = dp[i-1][j-1]
        else:    
            dp[i][j] = 1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
print(dp[len(s1)][len(s2)])


# misunderstood the question

