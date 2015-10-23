'''
You are given a square matrix of size N×N.
Calculate the absolute difference of the sums across the two main diagonals.

SAMPLE INPUTS:
3
11 2 4
4 5 6
10 8 -12
'''
def diagonals(size, matrix):
    ''' Takes size and all numbers in a matrix then returns the absolute value
        of the difference of the sums of the diagonals
    '''
    diag1 = 0
    diag2 = 0
    for i in range(0, size):
        diag1 = diag1 + matrix[i + size * i]
        diag2 = diag2 + matrix[(size -1) *(i + 1)]
    return abs(diag1 - diag2)

m_size = int(input())
matrix_in = ''
matrix_list = []
for i in range(0,m_size):
    matrix_in = matrix_in + ' ' + input()
matrix_list = list(map(int, matrix_in.split()))
print (diagonals(m_size, matrix_list))
