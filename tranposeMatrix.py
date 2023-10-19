# You're given a 2D array of integers matrix. Write a function that returns the transpose of the metrix. 

# The tanspose of a matrix is a flipped version of the original matrix across its main diagonal ( which runs from top-left to bottom-right); it switches the row and column indices of the original matrix. 

# You can assume the input matrix always has at least 1 value; however its width and height are not necessarily the same. 

# Sample Input

# Time complexity O(m * n) = O(n^2)

# matrix = [ [1, 2] ] 

# Sample Output :

# [ [1] , [2] ]


def transposeMatrix(matrix):
  #Write your code here
  transposeMatrix = []
  for col in range(len(matrix[0])):
    newRow = []
    for row in range(len(matrix)):
      newRow.append(matrix[row][col])
    transposeMatrix.append(newRow)  
  return transposeMatrix



# - You want to consider how to move through the inside columns of numbers 
# and the row of list. 


# In computer science, a matrix refers to a two-dimensional data structure consisting of rows and columns. It is used to represent and manipulate collections of values, such as numbers, characters, or other data types. A matrix is essentially a grid or a table with elements arranged in rows and columns.

# Each element in a matrix is identified by its row and column position, often denoted as (i, j), where 'i' represents the row number and 'j' represents the column number. The individual elements within the matrix can be accessed and manipulated using these indices.



# input matrix = [[1,2,3], [2,5,7], [8,9,6]]





# Time complextiy explained:


# The given code snippet calculates the transpose of a matrix. In the context of time complexity analysis, let's denote the number of rows in the original matrix as m and the number of columns as n. The code snippet has two nested loops:

# The outer loop runs for each column of the original matrix, iterating n times.
# The inner loop runs for each row of the original matrix, iterating m times.
# Inside the inner loop, there is a constant-time operation (accessing and appending elements to lists), which does not depend on the size of the matrix.

# Therefore, the overall time complexity of this code snippet is O(m * n), where:

# m is the number of rows in the original matrix.
# n is the number of columns in the original matrix.
# In the worst case, when the matrix is a square matrix (i.e., m equals n), the time complexity is O(n^2).






# Example of a problem use case: Rotate a square image by 90 degrees clockwise using matrix transposition: 


def rotate_image(matrix):
    if not matrix:
        return []

    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the 90-degree clockwise rotation
    for i in range(n):
        matrix[i] = matrix[i][::-1]

    return matrix

# Example usage:
image = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated_image = rotate_image(image)
for row in rotated_image:
    print(row)






# In this algorithm:

# We first transpose the original image matrix. Transposing means swapping elements across the main diagonal (from top-left to bottom-right). This step effectively turns rows into columns and columns into rows.

# After transposing, we reverse each row. This step completes the 90-degree clockwise rotation.

# The provided example rotates a 3x3 image, but the algorithm can be applied to images of different sizes as long as they are square (i.e., the number of rows equals the number of columns). This is a simplified version of image rotation; real-world image processing libraries use more efficient algorithms for image transformations and also handle non-square images and various interpolation methods for better quality