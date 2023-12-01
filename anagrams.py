# key takeaway here is how join and sorted work together. 

## sorted turns each item at each index in the words array into a list 
# join puts them back together into a string 
# join turns any interibale (list, set) into items into a string

words = ["car", "rac", "art", "tar"]


dict = {}

for word in words:

  sorted_W = ''.join(sorted(word)) # sorted turns strings into list and join turns that list into a string. 
  # word at index one is "car"
  # when car is inputed into sorted(word) it becomes ['a', 'c', 'r']
  # Then when it ' '.join(sorted(word)) it becomes "acr"

  if sorted_W in dict: #dic is empty
    dict[sorted_W].append(word)
  else: # if dic looks like this dic = {"arc": ["art",]} add "car" to it 
    dict[sorted_W] = [word]

print(list(dict.values()))       




# ___________________________________________________________________________


words = ["car", "rac", "art", "tar"]

dict = {}

for word in words:
  sorted_W = "".join(sorted(word))

  if sorted_W in dict:
    dict[sorted_W].append(word)
  else:
    dict[sorted_W] = [word]

print(list(dict.values()))