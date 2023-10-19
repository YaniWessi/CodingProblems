# It is New Year's Day and people are in line for the wonderland rollercoaster ride. 
# Each person wears a sticker indicating their initial position from 1 to n . 
# Any person can bribe the person directly in front of them to swap positions . 
#But! they still wear their original sticker. One person can bribe at most two others. 
#Determine the minimum number of bribes that took place to get to a given queue order. 
# Print the number of bribes, or , if anyone has bribed more than two people, print Too chaotic 


# def minimumBribes(q):
    # left = 0
    # right = 1
    # count = 0 
    # while left < len(q)-1:
    #     if q[left]+1 == q[right]:
    #         left += 1
    #         right += 1
    #     elif q[left] + 2 == q[right]:
    #         count = 1 
    #         swapper = q[right]
    #         left += 1
    #         right += 1 
    # return count 



# Secondone 


def minimumBribes(q):
   count = 0 
   for i in range(len(q)):
      if q[i] - (i + 1) > 2:
        print("Too chaotic")
        return
      for j in range(max(0, q[i] - 2), i):
        if q[j] > q[i]:
          count += 1

   print(count)           



q = [1, 2, 3, 5, 4, 6, 7, 8]


q = [4, 1, 2, 3]

