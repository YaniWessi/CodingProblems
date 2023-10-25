# You're given a two-demensional array(a matrix) of potentially unequal 
# height and width containing only 0 s and 1s. Each 0 represents land, 
# each 1 represents part of a river. A river consists of any number
# of 1s that are either horizontally or vertically adjacent(but not diagonally adjacent)
# . The number of adjacent 1 s forming a river determine its size. 

# Note that a river can twist. In other words, it doesn't have to be straight
# vertical line or a straight horizontal line; it can be L-shaped, for example

# Write a function that returns an array of the sizes of all rivers 
# represented in the input matrix. The sizes don't need to be in any particular
# order


def riverSizes(matrix):
    # Write your code here.
    sizes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0 or matrix[i][j] == -1:
                continue
            size = checkLeftBottom(i,j,matrix)
            sizes.append(size)
    return sizes 

def checkLeftBottom(i, j, matrix):
    if i >= len(matrix) or i < 0:
        return 0
    if j >= len(matrix[0]) or j < 0:
        return 0 

    if matrix[i][j] == 1:

        matrix[i][j] = -1
        right = checkLeftBottom(i+1, j, matrix)
        bottom = checkLeftBottom(i, j+1, matrix)
        left = checkLeftBottom(i-1, j, matrix)
        up = checkLeftBottom(i, j-1, matrix)

        return ( left + right + bottom + up + 1)
    return 0 




# The riverSizes function takes a 2D matrix (the input) as its parameter and returns a list of river sizes.

# It initializes an empty list called sizes to store the sizes of the rivers found in the matrix.

# It uses nested loops to iterate through each element of the matrix. For each element:

# If the element is 0 or already marked as -1, it skips to the next element.
# If the element is 1, it calls the checkLeftBottom function to explore and calculate the size of the river starting from this element.
# The checkLeftBottom function is a recursive function that explores a river from a given position (i, j) in the matrix.

# Within checkLeftBottom:

# If the current position (i, j) is out of bounds or is not a part of the river (value is 0), it returns 0.
# If the current position is part of the river (value is 1), it marks it as -1 to avoid double-counting and recursively explores the neighboring positions (right, bottom, left, and up).
# It calculates the size of the river by adding up the sizes of all connected 1s plus the current position (size = left + right + bottom + up + 1).
# The riverSizes function appends the calculated river size to the sizes list and continues the search for other rivers in the matrix.

# Finally, the function returns the list of river sizes.

# In summary, this algorithm recursively explores the matrix, marking and counting adjacent 1s to determine the size of each river and stores these sizes in a list, which is returned as the result.