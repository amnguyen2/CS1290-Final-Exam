# https://leetcode.com/problems/palindromic-substrings/
def countSubstrings(S):
    N = len(S)
    ans = 0
    # 2*N - 1, the pivot of a palindrome can be a letter or between two letters
    for center in range(2*N - 1): # move center point by 1
        left = center // 2 # left pointer moves every 2 iterations, but 1 faster than right pointer
        right = left + center % 2 # right pointer moves every 2 iterations
        
        # detect palindromic substrings between 'left' and 'right' pointers
        # while both ends of the current substring are the same letter, the palindrome continues
        while left >= 0 and right < N and S[left] == S[right]: # span over left index and right index
            ans += 1 # +1 more palindrome found
            left -= 1 # expand toward left
            right += 1 # expand toward right
    
    return ans
    
    
S = "abba"
print(countSubstrings(S))
