import random
import copy
import time
import sys
import os
import argparse

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

grid6 = [
    [0, 0, 6, 0, 0, 3],
    [5, 0, 0, 0, 0, 0],
    [0, 1, 3, 4, 0, 0],
    [0, 0, 0, 0, 0, 6],
    [0, 0, 1, 0, 0, 0],
    [0, 5, 0, 0, 6, 4]]

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2),
         (grid4, 2, 2), (grid5, 2, 2)]
'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''

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
                square += line
            squares.append(square)
    return (squares)

# To complete the first assignment, please write the code for the following function


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

    for i in range(n_rows*n_cols):
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


def find_empty(grid):
    '''
    This function returns the index (i, j) to the first zero element in a sudoku grid
    If no such element is found, it returns None

    args: grid
    return: A tuple (i,j) where i and j are both integers, or None
    '''

    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if grid[i][j] == 0:
                return (i, j)

    return None


def recursive_solve(grid, n_rows, n_cols):
    '''
    This function uses recursion to exhaustively search all possible solutions to a grid
    until the solution is found

    args: grid, n_rows, n_cols
    return: A solved grid (as a nested list), or None
    '''

    # N is the maximum integer considered in this board
    n = n_rows*n_cols
    # Find an empty place in the grid
    empty = find_empty(grid)

    # If there's no empty places left, check if we've found a solution
    if not empty:
        # If the solution is correct, return it.
        if check_solution(grid, n_rows, n_cols):
            return grid
        else:
            # If the solution is incorrect, return None
            return None
    else:
        row, col = empty

    # Loop through possible values
    for i in range(1, n+1):

        # Place the value into the grid
        grid[row][col] = i
        # Recursively solve the grid
        ans = recursive_solve(grid, n_rows, n_cols)
        # If we've found a solution, return it
        if ans:
            return ans

        # If we couldn't find a solution, that must mean this value is incorrect.
        # Reset the grid for the next iteration of the loop
        grid[row][col] = 0

    # If we get here, we've tried all possible values. Return none to indicate the previous value is incorrect.
    return None


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
    # Make a copy of the original grid
    filled_grid = copy.deepcopy(grid)

    # Loop through the rows
    for i in range(len(grid)):
        # Loop through the columns
        for j in range(len(grid[0])):
            # If we find a zero, fill it in with a random integer
            if grid[i][j] == 0:
                filled_grid[i][j] = random.randint(1, n)

    return filled_grid


def solve(grid, n_rows, n_cols):
    '''
    Solve function for Sudoku coursework.
    Comment out one of the lines below to either use the random or recursive solver
    '''

    # return random_solve(grid, n_rows, n_cols)
    return recursive_solve(grid, n_rows, n_cols)


def get_possible_values(grid: list[list[int]], n_rows: int, n_cols: int, row_index: int, col_index: int):
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


def delete_single_possible(grid: list[list[int]], converted_grid):
    found = False
    for i in range(len(converted_grid)):
        for j in range(len(converted_grid[i])):
            data = converted_grid[i][j]
            if isinstance(data, list) and len(data) == 1:
                #print("Put {0} in location({1},{2})".format(data[0],i,j))
                grid[i][j] = data[0]
                found = True
    return grid, found


def show_solution(solutions):
    for data in solutions:
        print(data)


def keep_delete_single(grid, n_rows, n_cols):
    flag = True
    new_grid = copy.deepcopy(grid)
    while flag:
        alternative_grid = convert_grid(new_grid, n_rows, n_cols)
        #show_solution(alternative_grid)
        new_grid, flag = delete_single_possible(new_grid, alternative_grid)
        #show_solution(new_grid)
        if flag == False:
            return new_grid


def choose_smallest_random(alternative_grid):
    # find smallest values
    length = 100
    # find smallest length
    for i in range(len(alternative_grid)):
        for j in range(len(alternative_grid[i])):
            data = alternative_grid[i][j]
            if isinstance(data, list):
                if length > len(data):
                    length = len(data)
    locations = []
    for i in range(len(alternative_grid)):
        for j in range(len(alternative_grid[i])):
            data = alternative_grid[i][j]
            if isinstance(data, list) and len(data) == length:
                locations.append([i, j])
                return i, j
    # choice = random.randint(0, len(locations)-1)
    # print(choice)
    # return locations[choice][0], locations[choice][1]


def recursive_solve_alternative(grid, n_rows, n_cols):
    '''
    This function uses recursion to exhaustively search all possible solutions to a grid
    until the solution is found

    args: grid, n_rows, n_cols
    return: A solved grid (as a nested list), or None
    '''
    grid = keep_delete_single(grid, n_rows, n_cols)
    # N is the maximum integer considered in this board
    n = n_rows*n_cols
    # Find an empty place in the grid
    empty = find_empty(grid)

    # If there's no empty places left, check if we've found a solution
    if not empty:
        # If the solution is correct, return it.
        if check_solution(grid, n_rows, n_cols):
            return grid
        else:
            # If the solution is incorrect, return None
            return None

    alternative_grid = convert_grid(grid, n_rows, n_cols)
    row, col = choose_smallest_random(alternative_grid)
    #print(row, col)

    possible_list = alternative_grid[row][col]
    #print("possible: ")
    #print(row, col, possible_list)
    if len(possible_list) == 0:
        #print("hello")
        return None
    # Loop through possible values
    for i in possible_list:

        # Place the value into the grid
        grid[row][col] = i
        # Recursively solve the grid
        ans = recursive_solve_alternative(grid, n_rows, n_cols)
        # If we've found a solution, return it
        if ans:
            return ans

        # If we couldn't find a solution, that must mean this value is incorrect.
        # Reset the grid for the next iteration of the loop
        grid[row][col] = 0

    # If we get here, we've tried all possible values. Return none to indicate the previous value is incorrect.
    return None


def main():
    print("grid5")
    show_solution(recursive_solve_alternative(grid5, 2, 2))
    print("grid6")
    show_solution(recursive_solve_alternative(grid6, 2, 3))
    print("easy1")
    show_solution(recursive_solve_alternative(grid_easy1, 3, 3))
    print("easy2")
    show_solution(recursive_solve_alternative(grid_easy2, 3, 3))
    print("easy3")
    show_solution(recursive_solve_alternative(grid_easy3, 2, 3))
    print("easy4")
    show_solution(recursive_solve_alternative(grid_med1, 3, 3))
    print("easy5")
    show_solution(recursive_solve_alternative(grid_med2, 3, 3))
    print("easy6")
    show_solution(recursive_solve_alternative(grid_hard1, 3, 3))

'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
'''


def test():

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
        show_solution(solution)
        if check_solution(solution, n_rows, n_cols):
            print("grid %d correct" % (i+1))
            points = points + 10
        else:
            print("grid %d incorrect" % (i+1))

    print("====================================")
    print("Test script complete, Total points: %d" % points)


if __name__ == "__main__":
    test()
    main()















 


    

