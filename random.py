
# Here's an example of how to import the mean function from the numpy package's
# statistics module:

from numpy import statistics

data = [1, 2, 3, 4, 5]
mean_value = statistics.mean(data)

# print(mean_value)



# To import a specific function from a module within a package,
# you can use the following syntax:

from package_name.module_name import function_name


# Alternatively, you can import only the specific function without
# importing the entire module:



from numpy.statistics import mean

data = [1, 2, 3, 4, 5]
mean_value = mean(data)

print(mean_value)




# In this case, we import only the mean function from the 
# statistics module within the numpy package. 
# This allows us to use the mean function 
# directly without needing to reference the module.






import pandas as pd

data = {'Name': ['John', 'Emily', 'Ryan'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Seattle', 'Chicago']}



df = pd.DataFrame(data)

# print(df)










from collections import defaultdict 

d = defaultdict(int)

words = ['apple', 'banana', 'apple', 'orange', 'banana']

for word in words:
  d[word] += 1


# print(d)



# Loops are used to: 
# - repative opporation 

# But when we work with a large number of iterations (millions/billions of rows) using loops is a crime 
# instead of loops in this case use vectorisation 

# what is vectorization
# The technique of implementing (NumPy) array operations on a dataset.
# In the background, it applies the operation to all the elements of an
# or series in one go( unlike a "for" loop that manipulates one row at a time)

# USE CASE 1: Finding the sum of numbers: 

# using a loop 

import time 
start = time.time()


# iterative sum 

total = 0 
# iterating through 1.5 Million numbers 
for item in range(0, 15000000):
  total = total + item 

print('sum is:' + str(total))
end = time.time()

print(end - start)

#1124999250000
#0.14 Seconds



# Using Vectorization 



import numpy as np 


start = time.time()

# vectorized sum - using numpy for vector 
# np.arange create the sequence of number 
print(np.arange(1500000))

end = time.time()

print(end - start)

#1124999250000

#0.008 Seconds 