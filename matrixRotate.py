# 1.6 Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

def matrixRotate (matrix,n):

    new_matrix = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(n):
        for j in range(n):
            new_matrix[i][j] = matrix[n - j - 1][i]

    return new_matrix


print matrixRotate([[1,2,3],[4,5,6],[7,8,9]],3)

# ou
# matrix = [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
# print  zip(*matrix[::-1])
