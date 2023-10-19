
words = ["car", "rac", "art", "tar"]


dict = {}

for word in words:

  sorted_W = ''.join(sorted(word))

  if sorted_W in dict:
    dict[sorted_W].append(word)
  else:
    dict[sorted_W] = [word]

print(list(dict.values()))       