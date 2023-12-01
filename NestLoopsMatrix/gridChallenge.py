
# Given a square grid of characters in the range ascii[a-z], rearrange elements
# of each row alphabetically, ascending. Determine if the columns are also in 
# ascending alphabetical order, top to bottom. Return YES if they are or NO if
#  they are not.



# My Solution 

# def gridChallenge(grid):
#     # Write your code here
#     for i in range(len(grid)):
#         sorted_grid = ''.join(sorted(grid[i]))
#         grid[i] = sorted_grid
        
#     index_in = 0 
#     item = len(grid) -1 
#     while index_in < item:
#         if grid[index_in][0] < grid[index_in + 1][0]:
#             index_in += 1 
#             continue
#         else:
#             return "NO"
#     return "YES"    


#The Better one

def gridChallenge(thing):
    # Sort each row alphabetically
    for row in range(len(thing)):
        sorted_row = ''.join(sorted(thing[i]))
    
    # Check if columns are in ascending alphabetical order
    for row in range(len(thing[0])):
        for col in range(len(thing) -1):
            if thing[row][col] > thing[row + 1][col]:
                return NO
    return YES 


# the column change first then the row change. 
# This setup is appropriate if you want to compare elements in the 
# same column but different rows in the if statement 
# (if grid[col][row] > grid[col + 1][row]).

# this appraoch is same row different col 

# for col in range(len(thing)):
#     for row in range(len(thing)-1):



thing  = ["abc", "ade", 'efg']



class Person:
    def __init__(self, firstName):
        self.firstName = firstName


# what I learned about the sorted function: 


# thing  = ["cba", "ead", 'gfe']

# sorted(thing[i]) those this -------> ['a', 'b', 'c] ['a','d','e'] ['e' , 'f' , 'g' ]
# join()--------> turns the sorted list into string. this ['a', 'b', 'c']---> "abc"

# This is how you have to think of range based on these examples. 

# thing  = ["abc", "ade", 'efg']

# range(len(thing))

# this means: from 0 1 2 exclusive of 3:

#range(len(thing)- 1)

# this means: len thing is 3 minus 1 which is 2. so 0 1 excluding 2

# example to think about: 

# for i in range(3):  # Outer loop
#     for j in range(2):  # Inner loop
#         print(f"Outer loop index: {i}, Inner loop index: {j}")


# Outer loop index: 0, Inner loop index: 0
# Outer loop index: 0, Inner loop index: 1
# Outer loop index: 1, Inner loop index: 0
# Outer loop index: 1, Inner loop index: 1
# Outer loop index: 2, Inner loop index: 0
# Outer loop index: 2, Inner loop index: 1
# Here's how it works:

# The outer loop runs with i taking values from 0 to 2.
# For each iteration of the outer loop, the inner loop runs with j taking values from 0 to 1.
# The inner loop completes its iterations for each value of i in the outer loop.
# This structure allows you to perform a certain task for every combination of
# values of the loop variables. In the context of matrices or 2D arrays, nested
# loops are often used to iterate over each element by iterating over rows and columns.