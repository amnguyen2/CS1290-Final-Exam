# Perfect Squares

### Recursive definition:
		The recursive definition of the problem is finding the minimum number of perfect squares that add up
	to n - 1. If I want to find the minimum number of perfect squares that add up to 4, for example, I need
	to find the solution to 3, then 2, then 1 and 0. I can use what I know starting from 0 and build up to n.
	The repeated step is calculating the output for each and every number leading up to n.
	
### Defining and combining sub-problems:
		I decided to start by breaking down the problem into sub-problems by every positive integer starting
	from 0 up to 'n'. I used an array of size n + 1, where 'n' is the input value. The first value in the 
	array is 0 and the rest is populated with 'math.inf' or the largest value available. I will edit the values 
	in the array after 0. Cell i = 1 in the array will contain 1 because it takes only 1 perfect squares to 
	add up to 1. Cell i = 2 in the array will contain 2 because it takes only 2 perfect squares to add up to 2.
	This pattern continues by adding up to 'n' to find a solution.

### Problem solving process:
		The problem asks to find the minimum number of perfect squares necessary to add up to 'n', any given
	value. I began by first considering the simplest problem. If I input 0, it's obvious that no other positive 
	integers add up to 0. If I input 1, my output would be 1 because 1 is a perfect square. This is true for all 
	inputs that are perfect squares. 1, 4, 9, and every other perfect square only requires the sum of 1 number 
	to add up to it (itself).
