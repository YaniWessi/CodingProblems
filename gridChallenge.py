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

def gridChallenge(grid):
    # Sort each row alphabetically
    for i in range(len(grid)):
        sorted_row = ''.join(sorted(grid[i]))
        grid[i] = sorted_row
    
    # Check if columns are in ascending alphabetical order
    for col in range(len(grid[0])):
        for row in range(1, len(grid)):
            if grid[row][col] < grid[row - 1][col]:
                return "NO"
    
    return "YES"



thing  = ["abc", "ade", 'efg']



class Person:
    def __init__(self, firstName):
        self.firstName = firstName


# what I learned about the sorted function: 

# sorted(grid[i]) those this -------> ['a', 'b', 'c] ['a','c','d'] ['e' , 'f' , 'g' ]
# grid[i] = sorted_string : put in back in its place 

