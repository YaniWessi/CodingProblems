# write a function that takes in a non-empty array of integers and returns an 
# array of the same length, where each element in the output array is equal to 
# the product of every other number in the input array. 

# In other words, the value at output[i] is equal to the product of every 
# number in the input array other than input[i]

def arrayOfProducts(array):
    # Write your code here.
    products = [1 for _ in range(len(array))]

    for i in range(len(array)):
        runningProduct = 1
        for j in range(len(array)):
            if i != j: 
                runningProduct *= array[j]
        products[i] = runningProduct
    return products 