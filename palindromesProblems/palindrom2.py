# given a string of lowercase letters in the range ascii[a-z], determine the
# index of a character that can be removed to make the string a palindrome.
# There may be more than one solution, but any will do. If the word is 
# already a palindrome of there is no solution, return -1. Otherwise, 
# return the index of a character to remove. 

# Example
# s = "bcbc"

# Either remove 'b' at index 0 or 'c' at index 3.

# def palindromeIndex(s):


def is_palindrome(s):
    return s == s[::-1]

def palindromeIndex(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            # Check which character to remove for a palindrome
            if is_palindrome(s[left + 1:right + 1]):
                return left
            elif is_palindrome(s[left:right]):
                return right
            else:
                return -1  # If no solution found

    return -1  # If the string is already a palindrome

# Example usage:
s = "bcbc"
result = palindromeIndex(s)
print(result)





Solution 2

def is_palindrome(s):
    return s == s[::-1]

def palindromeIndex(s):
    if is_palindrome(s):
        return -1  # Already a palindrome
    
    length = len(s)
    
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            # Try removing either character
            if is_palindrome(s[:i] + s[i + 1:]):
                return i
            elif is_palindrome(s[:length - 1 - i] + s[length - i:]):
                return length - 1 - i
            
    return -1  # No solution found

# Example usage:
s = "bcbc"
result = palindromeIndex(s)
print(result)
