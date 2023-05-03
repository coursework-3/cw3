import random
import copy
import time
import sys
import argparse
import matplotlib.pyplot as plt

# Grids 1-4 are 2x2
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

grid_easy3 = [
    [0, 3, 0, 4, 0, 0],
    [0, 0, 5, 6, 0, 3],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 0, 3, 0, 5],
    [0, 6, 4, 0, 3, 1],
    [0, 0, 1, 0, 4, 6]]

grid_easy1 = [
    [9, 0, 6, 0, 0, 1, 0, 4, 0],
    [7, 0, 1, 2, 9, 0, 0, 6, 0],
    [4, 0, 2, 8, 0, 6, 3, 0, 0],
    [0, 0, 0, 0, 2, 0, 9, 8, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 9, 4, 0, 8, 0, 0, 0, 0],
    [0, 0, 3, 7, 0, 8, 4, 0, 9],
    [0, 4, 0, 0, 1, 3, 7, 0, 6],
    [0, 6, 0, 9, 0, 0, 1, 0, 8]]

grid_easy2 = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]]

grid_hard1 = [
    [0, 2, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 6, 0, 4, 0, 0, 0, 0],
    [5, 8, 0, 0, 9, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 3, 0, 0, 4],
    [4, 1, 0, 0, 8, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 9, 5],
    [2, 0, 0, 0, 1, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 1, 0, 0, 8, 0, 5, 7]]

grid_med1 = [
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 0, 1],
    [3, 6, 9, 0, 8, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 6, 8, 0, 0],
    [0, 0, 0, 1, 3, 0, 0, 0, 9],
    [4, 0, 5, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 6, 0, 0, 7, 0, 0, 0],
    [1, 0, 0, 3, 4, 0, 0, 0, 0]]

grid_med2 = [
    [8, 0, 9, 0, 2, 0, 3, 0, 0],
    [0, 3, 7, 0, 6, 0, 5, 0, 0],
    [0, 0, 0, 4, 0, 9, 7, 0, 0],
    [0, 0, 2, 9, 0, 1, 0, 6, 0],
    [1, 0, 0, 3, 0, 6, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 3],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [5, 0, 0, 0, 0, 0, 0, 1, 4],
    [0, 0, 0, 2, 8, 4, 6, 0, 5]]

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2),
         (grid5, 2, 2), (grid_easy3, 2, 3), (grid_easy1, 3, 3),
         (grid_easy2, 3, 3), (grid_med1, 3, 3), (grid_med2, 3, 3),
         (grid_hard1, 3, 3)]

'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''


######################################################################
def check_section(section, n):

    if len(set(section)) == len(section) and \
            sum(section) == sum([i for i in range(n+1)]):
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
                square += line
            squares.append(square)

    return (squares)


def check_solution(grid, n_rows, n_cols):
    '''
    This function is used to check whether a sudoku board has been correctly
    solved

    args: grid - representation of a suduko board as a nested list.
    returns: True (correct solution) or False (incorrect solution)
    '''
    n = n_rows*n_cols

    for row in grid:
        if check_section(row, n) is False:
            return False

    for i in range(n_rows*n_cols):
        column = []
        for row in grid:
            column.append(row[i])

        if check_section(column, n) is False:
            return False

    squares = get_squares(grid, n_rows, n_cols)
    for square in squares:
        if check_section(square, n) is False:
            return False

    return True


def find_next_empty(puzzle):
    # finds the next row,col in the puzzle that is not filled--> rep with 0
    # return (row,col) tuple

    # keep in mind that we are using 0-8 for our indices

    for r in range(len(puzzle)):
        for c in range(len(puzzle[0])):

            if puzzle[r][c] == 0:
                return r, c

    return None, None


def is_valid(puzzle, guess, row, col, n_rows, n_cols):

    # checks whether the guess at the row/col of puzzle is valid guess
    # return True if is valid else False

    # start with row:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # now the column
    col_vals = []
    for i in range(len(puzzle)):
        col_vals.append(puzzle[i][col])

    if guess in col_vals:
        return False

    # n = int(len(puzzle)**0.5)
    # now the square
    row_start = (row//n_rows)*n_rows
    col_start = (col//n_cols)*n_cols

    for r in range(row_start, row_start+n_rows):
        for c in range(col_start, col_start+n_cols):
            if puzzle[r][c] == guess:
                return False

    return True


def recursive_solve(puzzle, r, c, max_hint=-1, explain=False,
                    output=sys.stdout):
    # puzzle is the list of lists where each innner list is a row in the puzzle
    # return whether solutin exists
    # mutates puzzle if solution exists

    # step1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step1.1: if there is nowhere left then we are done because we only
    # allowed valid inputs

    if row is None:
        return puzzle

    # step2: if there is place to put a number then we guess a number between
    # 1 and 9

    for guess in range(1, len(puzzle)+1):

        # step3: check if this is valid guess
        if is_valid(puzzle, guess, row, col, r, c):

            # step3.1: if this is valid then place the guess on the puzzle
            set_and_explain(puzzle, row, col, guess, max_hint, explain, output)
            # puzzle[row][col] = guess

            # now recurse using this puzzle
            # step4: recursively call the function
            ans = recursive_solve(puzzle, r, c, max_hint, explain, output)
            if ans:
                return ans

            # step5: if not valid then we need to backtrack and try new number
            set_and_explain(puzzle, row, col, 0,
                            explain=explain, output=output)

    # step6: if none of the numbers that work then it is not solvable
    return None


current_hint = 0

def show_solution(solutions, output=sys.stdout):
    '''
    print the grid to the output stream

    solutions: the grid
    output: the output stream
    '''
    for data in solutions:
        output.write(",".join([str(i) for i in data]))
        output.write("\n")


def set_and_explain(grid, row, col, value, max_hint=-1, explain=False, output=sys.stdout):
    '''
    set the value in the grid at location(row,col)
    print the solution if the hints is up to max
    '''
    global current_hint

    if value == 0:
        grid[row][col] = 0
        if current_hint > 0:
            current_hint -= 1
            if explain:
                output.write(
                    "Reset location({},{})\n".format(row, col))
        # print(current_hint)
    else:
        if max_hint < 0 or current_hint < max_hint:
            current_hint += 1
            grid[row][col] = value
            if explain:
                output.write(
                    "Put {} in location({},{})\n".format(value, row, col))
        else:
            show_solution(grid, output)
            output.close()
            sys.exit()



def get_possible_values(grid: list[list[int]], n_rows: int, n_cols: int,
                        row_index: int, col_index: int):
    '''
    get the possible values at row_index and col_index
    grid: the origin grid
    n_rows: row number
    n_cols: column number
    row_index: the row index
    col_index: the column index
    '''
    values = []
    # init
    for i in range(len(grid)):
        values.append(i+1)
    for value in grid[row_index]:
        if value != 0 and value in values:
            values.remove(value)
    for row in grid:
        for i in range(len(row)):
            if i == col_index:
                value = row[i]
                if value != 0 and value in values:
                    values.remove(value)
    squares = get_squares(grid, n_rows, n_cols)
    squares_index = ((row_index) // n_rows)*n_rows + ((col_index) // n_cols)
    # print(row_index, col_index, squares_index)
    for value in squares[squares_index]:
        if value != 0 and value in values:
            values.remove(value)
    return values


def convert_grid(grid: list[list[int]], n_rows: int, n_cols: int):
    '''
    convert the grid to the new grid with possible value list
    n_rows: the row number
    n_cols: the col number
    '''
    new_grid = []
    for i in range(len(grid)):
        line = []
        row = grid[i]
        for j in range(len(row)):
            if row[j] != 0:
                line.append(row[j])
            else:
                possible_values = get_possible_values(
                    grid, n_rows, n_cols, i, j)
                line.append(possible_values)
        new_grid.append(line)
    return new_grid


def delete_single_possible(grid: list[list[int]], converted_grid,
                           max_hint=-1, explain=False, output=sys.stdout):
    '''
    delete the single possible location in the grid

    grid: the original grid
    converted_grid: the converted grid
    max_hint: max of the hint
    explain: if need to provide instructions
    output: the output stream
    '''
    found = False
    for i in range(len(converted_grid)):
        for j in range(len(converted_grid[i])):
            data = converted_grid[i][j]
            if isinstance(data, list) and len(data) == 1:
                set_and_explain(grid, i, j, data[0], max_hint, explain, output)
                found = True
    return grid, found


def keep_delete_single(grid, n_rows, n_cols, max_hint=-1, explain=False,
                       output=sys.stdout):
    '''
    keep deleting the single possible locations

    grid: the original grid
    n_row: the row number
    n_cols: the col number
    max_hint: max of the hint
    explain: if need to provide instructions
    output: the output stream
    '''
    flag = True
    new_grid = copy.deepcopy(grid)
    while flag:
        alternative_grid = convert_grid(new_grid, n_rows, n_cols)
        # show_solution(alternative_grid)
        new_grid, flag = delete_single_possible(
            new_grid, alternative_grid, max_hint, explain, output)
        # show_solution(new_grid)
        if flag == False:
            return new_grid


def choose_smallest_random(alternative_grid):
    '''
    choose the next smallest location

    alternative_grid: the converted grid
    '''

    length = 100
    # find smallest length
    for i in range(len(alternative_grid)):
        for j in range(len(alternative_grid[i])):
            data = alternative_grid[i][j]
            if isinstance(data, list):
                if length > len(data):
                    length = len(data)
    # find locations
    locations = []
    for i in range(len(alternative_grid)):
        for j in range(len(alternative_grid[i])):
            data = alternative_grid[i][j]
            if isinstance(data, list) and len(data) == length:
                locations.append([i, j])
                # return i, j
    # choose next random location
    if len(locations) > 0:
        location = random.choice(locations)
        return location[0], location[1]
    return -1, -1


def alternative_solve(grid, n_rows, n_cols, max_hint=-1,
                                explain=False, output=sys.stdout):
    '''
    This function uses recursion to exhaustively search all
    possible solutions to a grid until the solution is found

    args: grid, n_rows, n_cols,max_hint,explain,output
    return: A solved grid (as a nested list), or None
    '''

    grid = keep_delete_single(grid, n_rows, n_cols, max_hint, explain, output)

    alternative_grid = convert_grid(grid, n_rows, n_cols)

    row, col = choose_smallest_random(alternative_grid)
    if row == -1:
        if check_solution(alternative_grid, n_rows, n_cols):
            return alternative_grid
        else:
            return None
        # print(row, col)

    possible_list = alternative_grid[row][col]
    # print("possible: ")
    # print(row, col, possible_list)
    if len(possible_list) == 0:
        # print("hello")
        return None
    # Loop through possible values
    for i in possible_list:

        # Place the value into the grid
        # grid[row][col] = i
        set_and_explain(grid, row, col, i, max_hint, explain, output)
        # Recursively solve the grid
        ans = alternative_solve(
            grid, n_rows, n_cols, max_hint, explain, output)
        # If we've found a solution, return it
        if ans:
            return ans

        # If we couldn't find a solution, that must mean this value is
        # incorrect.
        # Reset the grid for the next iteration of the loop
        set_and_explain(grid, row, col, 0, explain=explain, output=output)

    # If we get here, we've tried all possible values. Return none to
    # indicate the previous value is incorrect.
    return None

##########################################################################


def solve(grid, n_rows, n_cols, max_hint=-1, explain=False, output=sys.stdout):
    '''
    Solve function for Sudoku coursework.
    Comment out one of the lines below to either use the recursive solver
    or alternative

    grid: the grid
    n_rows: the row number
    n_cols: the column number
    max_hint: max of the hint
    explain: if need to provide instructions
    output: the output stream
    '''

    return alternative_solve(grid, n_rows, n_cols, max_hint, explain, output)
    # return recursive_solve(grid, n_rows, n_cols, max_hint, explain, output)


'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
'''


def run_profile():
    used_times = dict()
    used_times["recursive"] = []
    used_times["alternative"] = []
    grids2 = copy.deepcopy(grids)

    # calculate the recursive solver running time
    for (i, (grid, n_rows, n_cols)) in enumerate(grids):
        # print("Solving grid: %d" % (i+1))
        start_time = time.time()
        solution = recursive_solve(grid, n_rows, n_cols)
        elapsed_time = time.time() - start_time
        used_times["recursive"].append(elapsed_time*1000)
        # print("Solved in: %f seconds" % elapsed_time)
        # show_solution(solution)
        if not check_solution(solution, n_rows, n_cols):
            print("grid %d incorrect" % (i+1))

    # calculate the alternative solver running time
    for (i, (grid, n_rows, n_cols)) in enumerate(grids2):
        # print("Solving grid: %d" % (i+1))
        start_time = time.time()
        solution = alternative_solve(grid, n_rows, n_cols)
        elapsed_time = time.time() - start_time
        used_times["alternative"].append(elapsed_time*1000)
        # print("Solved in: %f seconds" % elapsed_time)
        # show_solution(solution)
        if not check_solution(solution, n_rows, n_cols):
            print("grid %d incorrect" % (i+1))

    # set and print the plot
    plt.plot(used_times["recursive"], label="recursive solver")
    plt.plot(used_times["alternative"], label="alternative solver")

    plt.title('different solutions running times')
    plt.xlabel('different grids')
    plt.ylabel('runnning time in microseconds')
    plt.xticks(range(11), ('2x2', '2x2', '2x2', '2x2', '3x2',
               '3x3', '3x3', '3x3', '3x3', '3x3', '3x3'))
    plt.legend()
    plt.savefig("profile.png")
    plt.show()

    print("profile complete")


def main():
    # add the arguments parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-file", dest="file", nargs=2)
    parser.add_argument("-hint", dest="hint", type=int)
    parser.add_argument("-explain", dest="explain",
                        action="store_true", default=False)
    parser.add_argument("-profile", dest="profile",
                        action="store_true", default=False)
    # parse the args
    args = parser.parse_args()
    explain_flag = args.explain
    max_hint = -1
    output_stream = sys.stdout
    if args.hint:
        max_hint = args.hint
    if args.profile:
        run_profile()
    # set the default grid with hard1
    default_grid = grid_hard1
    # parse the args file
    if args.file:
        input_file = args.file[0]
        output_file = args.file[1]
        output_stream = open(output_file, "w")
        grid = []
        with open(input_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                row = line.rstrip().split(",")
                grid.append([int(i) for i in row])
        default_grid = grid
    # get the row number and column number
    row = 3
    col = 3
    if len(default_grid) == 4:
        row = 2
        col = 2
    elif len(default_grid) == 6:
        row = 2

    show_solution(solve(default_grid, row, col, max_hint,
                  explain_flag, output_stream), output_stream)
    output_stream.close()


if __name__ == "__main__":
	main()