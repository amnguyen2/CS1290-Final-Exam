# Minimum Falling Path Sum

### Recursive definition:
		The recursive definition of the problem is

### Defining and combining sub-problems:
		I decided to start by breaking down the problem into sub-problems

### Problem solving process:
		The problem asks to  
	
	a) To break the problem down to it’s very first step, I start with the very first row of my 2D array. 
		The minimum path I can take to get to any of the cells on the first row is the same number, since I 
		can’t take any steps down, in this case. Because of this, I can make the new array’s first row the 
		same as the input array’s first row.
 	b) Then, once I’ve solved the first row, I now have to decide how I get to each cell in the row after the 
		first.
