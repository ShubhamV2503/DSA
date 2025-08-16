
## LeetCode Problem: Set Matrix Zeroes
## Leetcode Prblem number: 73
## TC:  O((N*M)*(N + M)) + O(N*M), 
## SC: O(1) - in place modification

# matrix = [[1,1,1],[1,0,1],[1,1,1]]
# # matrix = [[-1],[2],[3]]
# row  =  len(matrix)
# col = len(matrix[0])

# def mark_row(fixed_row):
#     for column in range(len(matrix[0])):
#         if matrix[fixed_row][column] != 0:
#             matrix[fixed_row][column] = 'check'
# def mark_col(fixed_col):
#     for row in range(len(matrix)):
#         if matrix[row][fixed_col] !=0:
#             matrix[row][fixed_col] = 'check'

# for i in range(row):
#     for j in range(col):
#         if matrix[i][j] == 0:
#             mark_row(i)
#             mark_col(j)

# for i in range(row):
#     for j in range(col):
#         if matrix[i][j] == 'check':
#             matrix[i][j] = 0
# print(matrix)


##-------------------------------------------------------------------

## TC O 2*(m*n)
## SC O(m)+O(n) - using extra space


# matrix = [[1,1,1],[1,0,1],[1,1,1]]

# row  =  len(matrix)
# col = len(matrix[0])

# r = [0]*row 
# c = [0] * col

# for i in range(row):
#     for j in range(col):
#         if matrix[i][j] == 0:
#             r[i] = 1
#             c[j] = 1

# for i in range(row):
#     for j in range(col):
#         if r[i] == 1 or c[j] == 1:
#             matrix[i][j] = 0

# print(matrix)


##---------------------------------------------

##TC: O(2*(N*M))
##SC: O(1)
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row  = len(matrix)
        col  = len(matrix[0])

        # Check if first column needs zeroing
        extra_col = 1
        for i in range(row):
            if matrix[i][0] == 0:
                extra_col = 0
                break

        # Mark zeros in first row/col
        for i in range(row):
            for j in range(1, col):  # skip first col
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero inner cells based on marks
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Handle first row
        if matrix[0][0] == 0:
            for j in range(col):
                matrix[0][j] = 0

        # Handle first column
        if extra_col == 0:
            for i in range(row):
                matrix[i][0] = 0