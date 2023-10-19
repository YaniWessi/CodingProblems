# Write a function that takes in an array of integers and returns a sorted version of
# that array. Use the Bubble Sort algorithm to sort the array 
#If you're unfamiliar with bubble sort, we recommend watching the conceptual Overview 
# section of this question's video explanation. 


def bubbleSort(array):
  # Write your code here to sort
  sort = False

  while not sort:
    sort = True
    for i in range(len(array)- 1):
      if array[i] > array[i+1]:
        array[i],array[i+1] = array[i+1], array[i]
        sort = False
  return array