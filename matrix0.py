# 1.7 Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column is set to 0.

def matrix0 (matrix):
    zero_rows = {}
    zero_columns = {}

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                zero_rows[i] = 0
                zero_columns [j] = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i in zero_rows or j in zero_columns:
                matrix[i][j] = 0

    return matrix

print matrix0([[1,2,3],[1,0,3],[1,2,3]])
