

items = [1,2,4,5,6,7,8]

dic = {}

for num in range(len(items)):
  dic[num] = items[num]


print(dic)



names = ["paul", "carl", "james", "adam"]

blend = {name: index for index, name in enumerate(names)}

print(blend)