
## LeetCode Problem: Set Matrix Zeroes
## Leetcode Prblem number: 73
## TC:  O((N*M)*(N + M)) + O(N*M), 
## SC: O(1) - in place modification

# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

# matrix = [[-1],[2],[3]]

# row  =  len(matrix)
# col = len(matrix[0])


# def mark_row(fixed_row):
#     for column in range(len(matrix[0])):
#         if matrix[fixed_row][column] != 0:
#             matrix[fixed_row][column] = 'a'
# def mark_col(fixed_col):
#     for row in range(len(matrix)):
#         if matrix[row][fixed_col] !=0:
#             matrix[row][fixed_col] = 'a'

# for i in range(row):
#     for j in range(col):
#         if matrix[i][j] == 0:
#             mark_row(i)
#             mark_col(j)


# for i in range(row):
#     for j in range(col):
#         if matrix[i][j] == 'a':
#             matrix[i][j] = 0
# print(matrix)


##---------------------------------------------

## TC O 2*(m*n)
## SC O(m)+O(n) - using extra space


# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

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

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

row  =  len(matrix)
col = len(matrix[0])

col_extra = 1

    # col0 = 1
    # for i in range(n):
    #     for j in range(m):
    #         if matrix[i][j] == 0:
    #             # mark i-th row:
    #             matrix[i][0] = 0

    #             # mark j-th column:
    #             if j != 0:
    #                 matrix[0][j] = 0
    #             else:
    #                 col0 = 0


for i in range(1,row):
    for j in range(1,col):
        if matrix[i][j] == 0:
            matrix[i][0] = 0

            if j != 0:
                matrix[0][j] = 0
            else:
                col_extra = 0

for i in range(1, row):
    for j in range(1, col):
        pass

