# https://leetcode.com/problems/palindromic-substrings/
def countSubstrings(S):
    N = len(S)
    ans = 0
    # 2*N - 1, the pivot of a palindrome can be a letter or between two letters
    for center in range(2*N - 1):
        left = center // 2
        right = left + center % 2
        print(left, center, right)
        while left >= 0 and right < N and S[left] == S[right]:
            ans += 1
            left -= 1
            right += 1
    return ans
    
    
S = "aaaa"
print(countSubstrings(S))