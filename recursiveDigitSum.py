# We define super digit of an interger x using the following rules:  

# Given an interger, we need to find the super digit of the integer. 
# if x has only 1 digit, then its super digit is x 
# Otherwise, the super digit of x is equal to the super digit of the sum of the digit of x. 



#my solution 

def superDigit(n, k):
  sum1 = 0 
  for num in range(len(n)):
    sum1 += int(n[num])

  if len(str(sum1)) == 1:
    return k
  else:
    return sum1    



# The working solution: 


def superDigit(n, k):
    if len(n) == 1:
        return int(n)  # Base case: single-digit number, return the digit itself
    
    sum1 = sum(int(num) for num in n)  # Sum the digits of n
    sum1 *= k  # Multiply the sum by k as per the problem description
    
    return superDigit(str(sum1), 1)  # Recursively calculate the super digit



n = '148'

k = 3


# this whole line 
      # for num in range(len(n)):
      #     sum1 += int(n[num])

# into this VV
          # sum1 = sum(int(num) for num in n)