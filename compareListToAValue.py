lis = [3, 5, 6, 7, 8, 9]
target = 3

dict = {"big": [], "small": []}

for num in range(len(lis)):
    if lis[num] > target:
        dict["big"].append(num)
    else:
        dict["small"].append(num)

print(dict)