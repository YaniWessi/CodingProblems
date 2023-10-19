
#Binary search 


seats = [1,2,3,4,5,6,7,8,9,10]

target = 9 

low = 0

high = len(seats) - 1 

for seat in range(len(seats)):
  mid = (high + low) // 2

  if seats[mid] == target:
    print(mid)
  elif seats[mid] > target:
    high = mid -1 
  else:
    low = mid + 1  