# Number of Arithmetic Slices

Define the problem/solution recursively (this is the most important step - if you don’t do this correctly, 
you will automatically get a 0 for the problem regardless of the code you write).

Briefly talk about how you plan to store solutions to sub-problems and combining them to solve the global problem 
(talk about the data structure/variables you’ll use to solve the problem).

IDEAL + Duke’s 7 steps

Upload everything to Github. Use readme files (one per problem) to do steps 1 and 2.


### Recursive definition:
		The recursive definition of the problem is comparing every 3 adjacent numbers in the input array.
	This is the action that is repeated about n times, where 'n' is the length of the input array. Once we 
	have compared the first 3 adjacent numbers, we move onto the next 3 adjacent numbers directly after 
	that. The size of the problem decreases by 1 with every step (n-1). Every time we compare, we record 
	the total number of arithmetic sequences found so far.

### Defining and combining sub-problems:
		My sub-problems are defined as every 3 adjacent numbers in my array. I traverse the entire array once,
	comparing the difference between first two and last two of every 3 adjacent numbers. I use an integer
	variable 'current' to count the number of contiguous groups of 3 arithmetic numbers. When an arithmetic
	sequence is found in the 3 numbers I compare, I count +1 to my 'current' variable and add the 'current'
	value to my total 'summation' value. 
		Remember that in an arithmetic sequence of length greater than 3, there is more than just 1 valid
	sequence that exists. 
	For example, in [7, 9, 11, 13], the valid arithmetic sequences are defined as:
		[7, 9, 11], [9, 11, 13], and [7, 9, 11, 13]

### Problem solving process:
		The problem asks to count the number of arithmetic sequences that exist in an array. A sequence (slice) 
	of numbers is considered arithmetic if it contains at least 3 elements and if the difference between any 2 
	consecutive elements of those 3 elements is the same. The space complexity of this solution is O(1), its 
	time complexity	is O(n), 'n' being the size of the input array.
	
	a)  I broke the problem down by considering the simplest versions of the problem I could think of, such as 
		an empty array and arrays of length less than 3. This is the easiest version of the problem because 
		I can determine instantly that an array of length less than 3 is not an arithmetic sequence, according to 
		the problem definition. 
	b)  I considered arrays of length 3, which would be my definitive sub-problem. I check every 
	    group of 3 adjacent numbers to determine whether those three are an arithmetic sequence by comparing the 
	    difference between the first 2 numbers and the last 2 numbers. I keep track of the number of arithmetic 
	    sequences I find up to this point using an integer variable. 
	c)	It's important to note that where there is an arithmetic sequence of length greater than 3, there is 
		more than just 1 arithmetic sequence to account	for. I keep track of these by using another integer variable 
		that, when I find more than one contiguous arithmetic sequence of length 3, I add 1 to my 'current' counter, 
		then add that number to my 'summation' counter. My 'current' counter will reset back to 0 if I find a 
		sequence of 3 numbers that are not arithmetic. This essentially means that an arithmetic sequence has ended.
