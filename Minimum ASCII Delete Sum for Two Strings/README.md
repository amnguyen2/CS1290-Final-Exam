# Minimum Falling Path Sum

### Recursive definition:
		The recursive definition of the problem is the repeated counting and deletion of letters in a string.
	For two non-empty strings, there are previous deletions of letters that should be considered. For example, 
	to find the difference in deletions between "aa" and "a", we should first find the difference in deletions 
	between "a" and "a". Before that, "" and "a". Before that, "" and "", two empty strings. The sum of the 
	ASCII values of deleted letters starts at 0 and accumulates with every progression of the problem toward
	a final solution.
	
### Defining and combining sub-problems:
		I decided to start by breaking down the problem into sub-problems by the individual letters of the 
	two strings. I compare every sub-string in the first string to every sub-string in the second string.
	I use an m*n 2D array to record the values that I'll need. When finding the minimal difference in deletions 
	between "ab" and "ac", I would need to delete "b" and "c". The simplest sub-string to compare within both
	of these strings are empty strings. After storing the difference in ASCII values between those two empty
	strings, I use that value to calculate the difference between "" and "a", then the difference between
	"" and "ac". By following this logic, I can find my final answer at the very lower-right corner of my
	m*n 2D array of values.
	

### Problem solving process:
		The problem asks to find the minimal sum of ASCII values accumulated when deleting letters of two
	strings to make them the same. For example, the output for the difference between "a" and "ab" will be
	98, because only "b" will be deleted. I will use a 2D array to store my ASCII values, the dimensions of
	the array will be m*n, where 'm' is the length of the first string plus 1, and 'n' is the length of the
	second string plus 1. This solution's space and time complexity are O(m*n), where 'm' is the length of 
	string one and 'n' is the length of string two.
		In my steps to solve this problem, I decided to use an example input to help my process and 
	explanation. I'm using the strings "delete" and "leet".
	
	a) To break the problem down, I start with the first row of my 2D array. In this row, I'm recording the 
		minimum difference in ASCII values between "" and "leet". The first cell will be 0, because the first
		column and first row represent an empty string. The second cell of the first row will contain the
		ASCII value of "l", the third cell will contain the ASCII value of "l" + "e", and so on. In this way,
		I can look at the first row of the table, and automatically output the difference between and empty
		string and any of the five sub-strings in "leet".
 	b) In the second row, instead of comparing an empty string to "leet", I'm comparing the first letter of
		"delete" to "leet". By viewing this row, I can output the difference in ASCII values between "d" and
		any of the five sub-strings in "leet". This pattern continues on for the next rows until the last
		letter of "delete".
	c) Before filling a cell with a value, I have to know what two strings I'm comparing respective to that cell.
		If the letters corresponding to the cell I'm on are the same, I won't have to delete that letter, so I
		can take advantage of my previous calculations in my table. For example, between "de" and "le", the output
		would only be the ASCII values of "d" + "l", because that "e" doesn't need to be removed. 
	d) If two letters that I'm comparing are different, however, I have to calculate a new value for the sub-strings 
		up to those letters. For example, as a simple case, to compare "d" and "l", I need to view other 
		previously calculated values. I would have to delete both of those letters, so I need to find the minimum 
		value in previous adjacent cells (which represent comparisons of "d"+"", ""+"l" and ""+""). I take the 
		minimum value in previous adjacent cells added to the values of "d" + "l".
