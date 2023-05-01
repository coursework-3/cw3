import random
import copy
import time

#Grids 1-4 are 2x2
grid1 = [
		[1, 0, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 3, 4],
		[3, 4, 2, 1]]

grid2 = [
		[1, 0, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 0, 4],
		[3, 4, 2, 1]]

grid3 = [
		[1, 0, 4, 2],
		[4, 2, 1, 0],
		[2, 1, 0, 4],
		[0, 4, 2, 1]]

grid4 = [
		[1, 0, 4, 2],
		[0, 2, 1, 0],
		[2, 1, 0, 4],
		[0, 4, 2, 1]]

grid5 = [
		[1, 0, 0, 2],
		[0, 0, 1, 0],
		[0, 1, 0, 4],
		[0, 0, 0, 1]]



grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2)]

'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''

def check_section(section, n):

	if len(set(section)) == len(section) and sum(section) == sum([i for i in range(n+1)]):
		return True
	return False

def get_squares(grid, n_rows, n_cols):

	squares = []
	for i in range(n_cols):
		rows = (i*n_rows, (i+1)*n_rows)
		for j in range(n_rows):
			cols = (j*n_cols, (j+1)*n_cols)
			square = []
			for k in range(rows[0], rows[1]):
				line = grid[k][cols[0]:cols[1]]
				square +=line
			squares.append(square)


	return(squares)

#To complete the first assignment, please write the code for the following function
def check_solution(grid, n_rows, n_cols):
	'''
	This function is used to check whether a sudoku board has been correctly solved

	args: grid - representation of a suduko board as a nested list.
	returns: True (correct solution) or False (incorrect solution)
	'''
	n = n_rows*n_cols

	for row in grid:
		if check_section(row, n) == False:
			return False

	for i in range(n_rows**2):
		column = []
		for row in grid:
			column.append(row[i])

		if check_section(column, n) == False:
			return False

	squares = get_squares(grid, n_rows, n_cols)
	for square in squares:
		if check_section(square, n) == False:
			return False

	return True







def random_solve(grid, n_rows, n_cols, max_tries=50000):
	'''
	This function uses random trial and error to solve a Sudoku grid

	args: grid, n_rows, n_cols, max_tries
	return: A solved grid (as a nested list), or the original grid if no solution is found
	'''

	for i in range(max_tries):
		possible_solution = fill_board_randomly(grid, n_rows, n_cols)
		if check_solution(possible_solution, n_rows, n_cols):
			return possible_solution

	return grid

def fill_board_randomly(grid, n_rows, n_cols):
	'''
	This function will fill an unsolved Sudoku grid with random numbers

	args: grid, n_rows, n_cols
	return: A grid with all empty values filled in
	'''
	n = n_rows*n_cols
	#Make a copy of the original grid
	filled_grid = copy.deepcopy(grid)

	#Loop through the rows
	for i in range(len(grid)):
		#Loop through the columns
		for j in range(len(grid[0])):
			#If we find a zero, fill it in with a random integer
			if grid[i][j] == 0:
				filled_grid[i][j] = random.randint(1, n)

	return filled_grid 

########################################################################################
def find_next_empty(puzzle):
    #finds the next row,col in the puzzle that is not filled--> rep with 0
    #return (row,col) tuple
    
    #keep in mind that we are using 0-8 for our indices
    
    for r in range(len(puzzle)):
        for c in range(len(puzzle[0])):
        
            if puzzle[r][c]==0:
                return r,c
                
    return None,None
    
    
def is_valid(puzzle, guess, row, col):
    
    # checks whether the guess at the row/col of puzzle is valid guess
    #return True if is valid else False
    
    #start with row:
    row_vals=puzzle[row]
    if guess in row_vals:
        return False
    
    # now the column
    col_vals=[]
    for i in range(len(puzzle)):
        col_vals.append(puzzle[i][col])
        
    if guess in col_vals:
        return False
        
    n=int(len(puzzle)**0.5)
    #now the square
    row_start=(row//n)*n
    col_start=(col//n)*n
    
    for r in range(row_start,row_start+n):
        for c in range(col_start,col_start+n):
            if puzzle[r][c]==guess:
                return False
                
    return True   
    
    
def recursive_solve(puzzle, r, c, max_hint=-1, explain=False, output=sys.stdout):
    
    #puzzle is the list of lists where each innner list is a row in the puzzle
    # return whether solutin exists
    #mutates puzzle if solution exists
    
    #step1: choose somewhere on the puzzle to make a guess
    row,col=find_next_empty(puzzle)
    
    #step1.1: if there is nowhere left then we are done because we only allowed valid inputs
    
    if row is None:
        return True
        
    #step2: if there is place to put a number then we guess a number between 1 and 9
    
    for guess in range(1,len(puzzle)+1):
        
        #step3: check if this is valid guess
        if is_valid(puzzle,guess,row,col,r,c):
            
            #step3.1: if this is valid then place the guess on the puzzle
            set_and_explain(puzzle, row, col, guess, max_hint, explain, output)
            puzzle[row][col]=guess
            
            #now recurse using this puzzle
            #step4: recursively call the function
            ans = recursive_solve(puzzle, r, c, max_hint, explain, output)
            if ans:
                return ans
                
        #step5: if not valid then we need to backtrack and try new number
        set_and_explain(puzzle, row, col, 0, explain=explain, output=output)
        
        
    #step6: if none of the numbers that work then it is not solvable
    return None


######################################################################################################

def solve(grid, n_rows, n_cols):

	'''
	Solve function for Sudoku coursework.
	Comment out one of the lines below to either use the random or recursive solver
	'''
	
	#return random_solve(grid, n_rows, n_cols)

	if recursive_solve(grid, n_rows, n_cols):
		return grid

	#return recursive_solve(grid, n_rows, n_cols)

	#if solve_sudoko(grid, n_rows, n_cols):
	#	return grid



'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
'''
def main():

	points = 0

	print("Running test script for coursework 1")
	print("====================================")
	
	for (i, (grid, n_rows, n_cols)) in enumerate(grids):
		print("Solving grid: %d" % (i+1))
		start_time = time.time()
		solution = solve(grid, n_rows, n_cols)
		elapsed_time = time.time() - start_time
		print("Solved in: %f seconds" % elapsed_time)
		print(solution)
		if check_solution(solution, n_rows, n_cols):
			print("grid %d correct" % (i+1))
			points = points + 10
		else:
			print("grid %d incorrect" % (i+1))

	print("====================================")
	print("Test script complete, Total points: %d" % points)


if __name__ == "__main__":
	main()
