# Neetcode roadmap, easy lebel for 2 pointers type questions


'''
A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
'''

# this solution feels like cheating.......


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        newStr = ""

        for char in s: 
            if char.isalnum(): # if charecter is alphanumeric
                newStr+= char.lower()

        
        return newStr == newStr[::-1]

        