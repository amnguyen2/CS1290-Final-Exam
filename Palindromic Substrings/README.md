# Minimum Falling Path Sum

### Recursive definition:
		This problem can be defined recursively by the comparison between characters of a substring, beginning
	from a center point. The string "aa" counts as a palindrome, but there also exists two more palindromic 
	substrings in "aa". This is the recursive nature of this problem. Where there exists a palindromic string
	of length greater than 1, there exists more than just 1 palindromic substring.
		
### Defining and combining sub-problems:
		I decided to start by breaking down the problem into sub-problems by defining a center point of any
	possible palindrome. The number of center points is always 2*n - 1, where 'n' is the length of a string.
	We can iterate through every possible center point and, for each center point, use two pointers to detect
	palindromes. The 'left' and 'right' pointers both start from the center point and expand to either side of
	the substring, comparing both ends of the substring. For every valid palindromic substring, we add 1 to a
	counter.
    
### Problem solving process:
		The problem asks to count the number of palindromes that exist within a given string. A string is
	considered a palindrome when it can be read the same way forward as it is read backward. For example, 
	the string "abba" contains 6 palindromic substrings. These include "a", "b", "b", "a", "bb", and "abba".
	
	a) A major factor in defining a palindrome is its center. In other words, a palindrome can be identified 
		by reading a word from its center to the left, and from its center to the right. If these "mirrored" 
		substrings are identical, the string is a palindrome. In a given string, there exists 2*n - 1 possible 
		center points. A center point can be a letter or an empty string between two letters.
	b) From every possible center point, we can scan and expand to find any possible palindromes in a string. 
		From a center point, we can use two iterating "pointers", 'left' and 'right', to detect palindromes.
		As long as the characters where the left and right pointers are at are both the same, the palindrome
		continues.
