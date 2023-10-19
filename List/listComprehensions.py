# a way to create lists based on existing lists or other iterable objects. This
# perform various operations on the element of the original iterable and create a new list in a single line of code 


# Filtering elements: 

from ast import comprehension


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [x for x in numbers if x % 2 == 0]







# Applying transformations: 

names = ["Alice", "Bob", "Charlie"]

uppercased_names = [name.upper() for name in names]




# List of names into their length 

names = ["Adam", "Pac", "Steve", "Smith"]

length = [len(name) for name in names]

# print(length)








# Nested list comprehensions: 

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened_matrix = [element for row in matrix for element in row]







#Mathematical operations:

numbers = [1, 2, 3, 4, 5]

squared_numbers = [x ** 2 for x in numbers]







#String operations:

words = ["apple", "banana", "cherry"]

word_lenghths = [len(word) for word in words]








# Conditional expression: List comprehensions can include conditional expressions to conditionally include elements in the new list. 


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_numbers = [x if x % 2 == 0 else x * 2 for x in numbers]







# Set operations: List comprehension can also be used to perform set operations, such as creating a list  of unique elements. 

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

unique_numbers = list({x for x in numbers})



# In a list of strings remove part of the string that

links = [
  "www.b001.io",
  "www.youtube.com",
  "www.wikipedia.org"
]

# removeprefix removes the sub string from the left side 

for link in links:
  print(link.removeprefix("www."))