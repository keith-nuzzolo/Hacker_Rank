'''
Given a 2D array of digits,
try to find the location of a given 2D pattern of digits.

Sample Input:
1
10 10
7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137
3 4
9505
3845
3530
'''
def create_grid(rows, columns):
    '''
    Takes the number of rows and columns and creates a grid based on
    user inputs
    '''
    return [input() for line in range(int(rows))]

def test_case(grid, row_start, column_start, grid_pattern):
    '''
    Takes in a pattern and a grid to test starting with the inputed row and
    column. Returns whether the pattern exists in the grid at the specified row
    and column pair.
    '''
    column_iter = column_start
    row_iter = row_start
    for row in range(len(grid_pattern)):
        for column in range(len(grid_pattern[0])):
            if grid[row_iter][column_iter] != grid_pattern[row][column]:
                return False
            column_iter += 1
        column_iter = column_start
        row_iter += 1
    return True



def test_grid(grid, grid_pattern):
    '''
    Tests whether a grid pattern exists within a given grid
    '''
    rows_to_test = len(grid) - len(grid_pattern)+1
    columns_to_test = len(grid[0]) - len(grid_pattern[0])+1
    for row in range(rows_to_test):
        for column in range(columns_to_test):
            if test_case(grid,row,column, grid_pattern):
                return True
    return False


def grid_search():
    '''
    Takes user input for number of test cases then builds that many
    new grids for each test case. Returns YES if the pattern grid is in
    the grid and NO if it is not.
    '''
    number_of_test_cases = int(input())
    answers = []
    for test_number in range(number_of_test_cases):
        temp = input().split()
        grid_length = temp[0]
        grid_height = temp[1]
        grid = create_grid(grid_length, grid_height)
        temp2 = input().split()
        pattern_length = temp2[0]
        pattern_height = temp2[1]
        grid_pattern = create_grid(int(pattern_length), int(pattern_height))
        if test_grid(grid, grid_pattern):
            answers.append('YES')
        else:
            answers.append('NO')
    [print(x) for x in answers]
grid_search()
