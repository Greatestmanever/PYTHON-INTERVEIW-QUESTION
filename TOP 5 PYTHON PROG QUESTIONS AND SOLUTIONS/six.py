# Write a Python program to check whether a string is a Palindrome or not(Hint: A palindrome is a word, phgase, number or sequence of words that reads the same backword or forward. e.g. Madam)

def ispalindrome(s):

    #Using predefined function to
    # Reverse to string print(s)

    rev = ''.join(reversed(s))

    # Checking if both string are
    # equal or not

    if (s == rev):
        return True
    return False
    
ispalindrome("level")