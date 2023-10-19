# Transform the a list of names into a dictionary with names and length 

names = ["Adam", "Steve", "Charles", "Jackson"]

length = {name:len(name) for name in names}

print(length)