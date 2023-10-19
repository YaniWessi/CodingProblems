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













r = "aaab"

print(palindromeIndex(r))



def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1

    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True





def palindromeIndex(string):
    rIndex = 0
    lIndex = len(string) - 1

    while rIndex < lIndex:
        if string[rIndex] != string[lIndex]:
            return False
        rIndex += 1
        lIndex -= 1 
    return True                      