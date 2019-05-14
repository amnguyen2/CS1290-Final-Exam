# https://leetcode.com/problems/minimum-falling-path-sum
def minFallPathSum(arr):
    n = len(arr)
    # create an array the same size as 'arr'
    dp = [[None] * n for i in range(n)]
    # first row is identical, simple example of the problem when broken down
    dp[0] = arr[0]
    for i in range(1, n): # start at second row
        for j in range(n):
            dp[i][j] = arr[i][j] # always add the respective cell's value
            
            # if-statements are used to manage index errors
            if j == 0: # if at first cell in a row, there are 2 choices
                dp[i][j] += min(dp[i-1][j], dp[i-1][j+1])
            
            elif j == n-1: # if at last cell in a row, there are 2 choices
                dp[i][j] = arr[i][j] + min(dp[i-1][j], dp[i-1][j-1])
            
            elif j > 0 and j < n-1: # otherwise, there are 3 choices
                dp[i][j] = arr[i][j] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
    
    return min(dp[-1]) # return the sum of the shortest path to the bottom
    
###############################################################################
arr = [[1, 2, 3, 4],
       [4, -1, 3, -2], 
       [-2, 5, -3, 2],
       [7, -6, 9, 8]]

print(minFallPathSum(arr))














