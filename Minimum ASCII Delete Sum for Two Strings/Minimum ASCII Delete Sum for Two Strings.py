# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
def minimumDeleteSum(s1, s2):        
        l1 = len(s1)
        l2 = len(s2)
        # create l1+1 * l2+1 2D list of 0's
        dp = [[0] * (l2+1) for l in range(l1 + 1)]
            
        for j in range(1, l2 + 1): # fill the first row from j=1 to end.
            # every dp[0][j] will be its letter's ASCII value + every previous letter's ASCII value
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
        
        for i in range(1, l1 + 1): # fill the first column from i=1 to end.
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
            
            for j in range(1, l2 + 1):
                # compare every letter of both words to one another
                if s1[i - 1] == s2[j - 1]: # if two letters are the same...
                    # ...use the same previously calculated value
                    dp[i][j] = dp[i - 1][j - 1] 
                else: # if two letters are different...
                    # ...take the path of minimum possible number of deletions 
                    dp[i][j] = min(dp[i][j - 1] + ord(s2[j - 1]), dp[i - 1][j] + ord(s1[i - 1]))
        return dp[-1][-1]
###############################################################################

s1 = "delete"
s2 = "leet"

print("minimumDeleteSum:", minimumDeleteSum(s1, s2))