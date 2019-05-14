# https://leetcode.com/problems/arithmetic-slices/

# A sequence (slice) of numbers is considered arithmetic if it contains at 
# least 3 elements and if the difference between any two consecutive elements
# is the same.
# Note: Where there are consecutive arithmetic slices, there are more than 2
#       arithmetic slices. For example: In [7, 9, 11, 13], the arithmetic 
#       slices are [7, 9, 11], [9, 11, 13], and [7, 9, 11, 13].
def numberOfArithmeticSlices(A):
    curr = 0 # number of consecutive arithmetic slices found
    sum = 0 # total number of consecutive arithmetic slices found
    
    for i in range(2,len(A)):
        # compare 3 adjacent values
        if A[i]-A[i-1] == A[i-1]-A[i-2]: # if these 3 values are arithmetic...
            curr += 1 # keep track of the number of consecutive arithm. slices. 
            sum += curr # ...record the total number of arithm. slices found UP TO THIS POINT
       
        else: # if these 3 values are NOT arithmetic
            curr = 0 # reset the number of consecutive arithm. slices to 0

    return sum # return the accumulative number of arithm. slices

###############################################################################
A = [1, 3, 5, 7, 9]

print("result:", numberOfArithmeticSlices(A))





