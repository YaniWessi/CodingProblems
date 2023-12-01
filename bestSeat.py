# Initialize variables bestSeat and maxSpace to keep track of the best seat and the maximum available space, both initially set to -1.

# Initialize a variable left to 0, which represents the current leftmost seat being considered.

# Start a while loop that continues as long as left is less than the length of the seats array.

# Inside the loop, initialize right as left + 1, representing the seat immediately to the right of the current leftmost seat.

# Start another while loop that continues as long as right is less than the length of the seats array and the seat at the right position is unoccupied (denoted by 0).

# Increment right until an occupied seat is encountered or the end of the row is reached.

# Calculate the availableSpace as the difference between right and left minus 1.

# If the availableSpace is greater than the current maxSpace, update bestSeat to be the midpoint between left and right, and update maxSpace to be the new maximum available space.

# Set left to the current right position, preparing for the next iteration.

# Continue the outer while loop until all seats are considered.

# Return the bestSeat, which represents the optimal seat with the maximum available space on either side.






# Pointer Manipulation: The use of left and right pointers to traverse the array efficiently.
# Looping Techniques: The algorithm employs nested while loops for iteration through the seat array.
# Conditional Statements: The algorithm uses conditional statements to check seat occupancy and update the best seat.
# Math Operations: The calculation of the midpoint between left and right is performed using the formula (left + right) // 2.
# Understanding of Indices: Proper handling of array indices, considering edge cases and avoiding index out-of-bounds errors.
# When tackling similar problems, focus on efficient iteration, careful management of pointers, and handling edge cases. Understanding the problem statement and developing a clear mental model of the solution can guide you in choosing appropriate data structures and algorithms.


def bestSeat(seats):
  bestSeat = -1 
  maxSpace = 0 

  left = 0 
  while left < len(seats):
    right = left + 1
    while right < len(seats) and seats[right] == 0:
      right += 1
    availableSpace = right - left - 1
    if availableSpace > maxSpace:
      bestSeat = (left + right) // 2 
      maxSpace = availableSpace
    left = right 
  return bestSeat      



seats = [1, 0, 1, 0, 0, 0, 1]


