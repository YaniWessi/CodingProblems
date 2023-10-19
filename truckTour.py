# Suppose there is a circle. There are N petrol pumps on that circle. 
# Petrol pumps are numbered 0 to (N - 1) (both inclusive)> You have tow pieces
# Of information corresponding to each of the petrol pump: (1) the amount 
# petrol the particular petrol pump will give, and (2) the distance form that 
# petrol pump to the next petrol pump. Initially 
# , you have a tack of infinite capacity carrying no petrol. 
# You can start the tour at any of the petrol pumps. 
# Calculate the first pint from where the truck will be able
#  to complete the circle. Consider that the truck will stop
# At each of the petrol pumps. The truck will stop at each of 
# the petrol pumps. The truck will move one limo force liar of the petrol


# Input first line will contain the value of N.
# The next N line will contain a pair of integers. 
# I.e the amount of petrol that petrol pump will give 
# and distance between that petrol pump and the next petrol pump. 

# OUT PUT: 

# An integer which will be the smallest index of the petrol pumps:


# Here is my solutions:
 

# My though process was: 
#  - loop through the all of the petrol stations and say if the amout of petrol is 
#  greater then the distance and the amout of station in the circle. 
#  return the the index that is where the amount of gas is greater then distance and len of stations. 
#  my approach was wrong: 


def truckTour(lst):
  for i in range(0, len(lst)):
    if lst[i][0] >= lst[i][1] and len(lst):
      return i 



# _____________________________________________________________________________

# Explanation:

# Initialize start_index and petrol variables to keep track of the starting index and the current petrol amount.
# Iterate through each petrol pump in the lst list.
# Calculate the difference between the petrol given by the current pump (lst[i][0]) and the distance to the next pump (lst[i][1]), and add it to the petrol variable.
# If petrol becomes negative, it means we cannot reach the next pump from the current starting point. So, update the start_index to the next pump's index (i + 1) and reset petrol to 0.
# After iterating through all the pumps, the start_index will store the smallest index of the petrol pump from where the truck can complete the circle.
# Return the start_index as the result.
# In the provided example, the output will be 1, indicating that the truck can start from the petrol pump at index 1 ([10, 3]) and complete the circle successfully.

def truckTour(petrolpumps):
  start_index = 0 

  petrol = 0 

  for i in range(len(petrolpumps)):
    petrol += petrolpumps[i][0] - petrolpumps[i][1]
    if petrol < 0:
      start_index = i + 1 
      petrol = 0 
  return start_index    



lst = [[1, 5], [10, 3], [3, 4]]
result = truckTour(lst)
print(result)