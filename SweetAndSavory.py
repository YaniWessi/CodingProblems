# You're hosting an event at a food festival and want to showcase the best 
# possible pairing of two dishes fromt the festival that complement each other
# flavor profile. 

# Each dish has a flavor profile represented by an integer. A negative integer
# means a dish is sweet, while a positive of -3 is slightly sweet, one of -10 
# is extremely sweet, one of 2 is mildly savory, and one of 8 is significantly 
# savory. 

# You're given an array of these dishes and a target combined flavor profile.
# Write a function that returns the best possible pairing of two dishes
# (the pairing with a total flavor profile that's closest to the target one). 
# Note that this pairing must include one sweet and one savory dish. You're also 
# concerned about the dish being too savory, so your pairing should never be 
# more savory than the target flavor profile. 

# All dishes will have a positive or negative flavor profile; there are no dishes
#  with a 0 value. For simplicity,you can assume that there will be at most one best 
#  solution, your function should return [0, 0]. The returned array should be sorted 
#  meaning the sweet dish should always come first. 

def sweetAndSavory(dishes, target):
   #Write your code here 
   return[]