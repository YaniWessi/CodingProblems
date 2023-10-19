#https://www.geeksforgeeks.org/python-collections-module/



from collections import defaultdict 

text = "hello world"

char_count = defaultdict(int)

for char in text:
  char_count[char] += 1


for char, count in char_count.items():
  print(char, count)