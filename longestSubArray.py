# My appraoch didn't work 


# def longestSubarrayWithSum(array, targetSum):
#   left = 0 
#   right = len(array) - 1 

#   for num in array:
#     if sum(array) == targetSum:
#       return[array[0], array[len(array)-1]]
#     elif sum(array[left+1:right]) == targetSum:
#       return[num] 
#     else:
#       left += 1 
#       right -= 1

#   return []       






#they approach that worked: 

# def longestSubarrayWithSum(array, targetSum):
#   indices = []

#   currentSubarraySum = 0 
#   startingIndex = 0 
#   endingIndex = 0 

#   while endingIndex < len(array):
#     currentSubarraySum += array[endingIndex]


#     while startingIndex < endingIndex and currentSubarraySum > targetSum:
#       currentSubarraySum -= array[startingIndex]
#       startingIndex += 1

#     if currentSubarraySum == targetSum:
#       if len(indices) == 0 or indices[1] < endingIndex - startingIndex:
#         indices = [startingIndex, endingIndex]

#       endingIndex += 1

#   return indices            






# A third solution 

def longestSubarrayWithSum(array, targetSum):
  indices = []

  for startingIndex in range(len(array)):
    currentSubarraySum = 0 

    for endingIndex in range(startingIndex, len(array)):
      currentSubarraySum += array[endingIndex]

      if currentSubarraySum == targetSum:
        if len(indices) == 0 or indices[1] - indices[0] < endingIndex - startingIndex:
          indices = [startingIndex, endingIndex]

  return indices


