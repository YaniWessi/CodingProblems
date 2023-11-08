# Using Pointers to Check for Palindromes
# ----------------------------------------

# In computer programming, pointers are memory addresses that allow us to access data in a more efficient way. 
# We can use pointers to check whether a given string is a palindrome, a sequence that reads the same backward as forward.

# We start by defining two pointers, `leftIdx` and `rightIdx`, which initially point to the leftmost and rightmost characters in the string, respectively.
# These pointers help us compare characters from the outer edges of the string towards the center.

def isPalindrome(string):
    leftIdx = 0                   # Initialize the left pointer to the start of the string.
    rightIdx = len(string) - 1    # Initialize the right pointer to the end of the string.

    while leftIdx < rightIdx:     # We use a while loop to keep comparing characters as long as the left pointer is less than the right pointer.
        if string[leftIdx] != string[rightIdx]:  # If the characters at the left and right pointers don't match, the string is not a palindrome.
            return False
        leftIdx += 1              # Move the left pointer one step to the right.
        rightIdx -= 1            # Move the right pointer one step to the left.

    return True                 # If the loop completes without finding any mismatch, the string is a palindrome.

# This code effectively uses two pointers and a while loop to compare characters and determine whether the input string is a palindrome.


#Time complexity

# Space complexity is linnear 

# time is O(n) linear time 


#---------------------------------------------------------------------------------------------------------------------------------------------------




def palindromeIndex(string):
    rIndex = 0
    lIndex = len(string) - 1

    while rIndex < lIndex:
        if string[rIndex] != string[lIndex]:
            return False
        rIndex += 1
        lIndex -= 1 
    return True                      






    # def palindromeIndex(s):
#     # Write your code here
    
#     if s[:] == s[::-1]:
#         return -1 
    
#     start_index = 1
#     excluded_index = 0
    
#     for i in range(len(s)):
#         if s[start_index:] == s[-1:excluded_index:-1]:
            
#             start_index += 1
#             excluded_index += 1
#             return i 
#         start_index += 1
#         excluded_index += 1
#     return -1 






def palindromeIndex(s):
    if s[:] == s[::-1]:
        return -1 
    
    left_index = 0
    right_index = len(s) - 1
    
    while left_index < right_index:
        if s[left_index] != s[right_index]:
            # Check if excluding left character makes the string a palindrome
            if s[left_index + 1 : right_index + 1] == s[left_index + 1 : right_index + 1][::-1]:
                return left_index
            
            # Check if excluding right character makes the string a palindrome
            if s[left_index : right_index] == s[left_index : right_index][::-1]:
                return right_index
            
            # If neither exclusion makes the string a palindrome, return -1
            return -1
        
        left_index += 1
        right_index -= 1
    
    return -1