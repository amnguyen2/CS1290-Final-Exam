# Minimum Falling Path Sum

### Recursive definition:
		The recursive definition of the problem is comparing the possible paths you could have taken to 
	get to a given cell. To find the minimum possible path to a cell, I have to know what path I took to 
	get there. That is the repeated step. If I want to make it to a specific cell, what possible step could 
	I have taken before it (n-1)? This is the question that must be asked to come to the recursive definition 
	of the problem. For example, if I want to know the minimum sum of the path to get to cell arr[2, 2], 
	I would compare the only three cells that can be ‘walked’ on before cell arr[2, 2]. Those three cells 
	are my choices, which would be arr[1, 1], arr[1, 2], and arr[1, 3].

### Defining and combining sub-problems:
		I decided to start by breaking down the problem into sub-problems by dividing my input 2D array 
	into rows of values. The problem can then be broken down further into individual cells. I can use the 
	cells of the array to represent a path leading up to that cell (starting from any cell in the first row). 
	Each cell contains the minimal accumulation of the values in the path up to that cell. Each cell's value 
	depends on the values in the row before that cell. That is the definition of the sub-problems and how 
	they are stored individually. Now, what I'm looking for is a path from any cell in the first row, to any 
	cell in the last row of the 2D array. Given this context, I can use my newly created 2D array of solutions 
	to my sub-problems. I'll access the last row and find the minimum value of that row, which is the solution 
	to the global problem.

### Problem solving process:
		The problem asks to compare possible paths to find the minimum possible sum going from the top 
	of a square grid to its bottom. I’ll start with the first row, and make my way down to the bottom, making 
	decisions of where to go based on previous decisions. I decided to try to solve the problem by breaking 
	it down into parts. I will use a 2D array that is the exact same size as the original input 2D array. 
	
	a) To break the problem down to it’s very first step, I start with the very first row of my 2D array. 
		The minimum path I can take to get to any of the cells on the first row is the same number, since I 
		can’t take any steps down, in this case. Because of this, I can make the new array’s first row the 
		same as the input array’s first row.
 	b) Then, once I’ve solved the first row, I now have to decide how I get to each cell in the row after the 
		first. If I start at the first cell last cell of this second row, I have 2 choices of where I could 
		have ‘walked’ before arriving at this cell. At any other cell on this row, besides the first and 
		last, I have 3 possible paths I could have taken. 
	c) At a given cell arr[i, j], to find the minimum path leading up to that cell, I have to check the 
		adjacent cells in the row before. So, I would be looking at arr[i-1, j-1], arr[i-1, j], and 
		arr[i-1, j+1]. I will use the minimum value among these 3 possible paths. Like I mentioned before, 
		if I’m at the first cell of a row, I would only check arr[i-1, j] and arr[i-1, j+1]. 
		Similarly, if I’m at the last cell of a row, I would only check arr[i-1, j] and arr[i-1, j-1]. 
		In my new 2D array, in the cell I’m on, I will enter the minimum value of the 2 or 3 possible 
		choices I have made in the previous row, added to the respective cell of the input 
		2D array (the cell I’m on).
	d) I fill the entire 2D array, row by row, using a row’s previous values. Once the entire array is filled, 
		I can access any cell and output the minimum possible path’s sum of values by returning that cell’s 
		value. The value I’m looking for, for this problem, is in the very last row. I’m looking for the 
		minimum possible path’s sum from the first row to the last row. I search the last row of my new 
		2D array for the minimum possible value and return that value.
