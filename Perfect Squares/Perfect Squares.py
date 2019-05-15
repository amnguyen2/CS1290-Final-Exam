# https://leetcode.com/problems/perfect-squares/
import math

def numSquares(n):
    # create array of [0, inf, inf, ... inf], we are searching for a minimum value
    dp = [math.inf]*(n+1)
    dp[0] = 0
    
    for i in range(1, n+1, 1):
        sqrt = int(math.sqrt(i))
        
        # if 'i' is already a perfect square, then dp[i] can be 1.
        if sqrt*sqrt == i:
            dp[i] = 1
        
        for j in range(1, sqrt+1, 1):
            dif = i - j*j

            dp[i] = min(dp[i], (dp[dif]+1))
        # https://leetcode.com/problems/perfect-squares/discuss/71605/Java-DP-Solution-with-explanation   
        print()
            
    print(dp)
    
    return dp[n]
    
###############################################################################
    
n = 8

print(numSquares(n))