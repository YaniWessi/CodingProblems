# You're given an unordered list of unique integers nums in the range [1, n], 
# where n represents the length of nums + 2. This means that two numbers in 
# this range are missing from the list. 

# Write a function that takes in this list and returns a new list with the two
# missing numbers, sorted numerically. 


def missingNumbers(nums):

  compare_list = []

  for num in range(1, len(nums) +3):
    compare_list.append(num)


  for i in range(len(nums)):
    if nums[i] in compare_list:
      compare_list.remove(nums[i])


  return sorted(compare_list)



nums = [1, 4, 3]

