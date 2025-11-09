# neetcode roadmap, easy level in the Arrays and Hashing category


'''
time complexity of this is o(n)

could be o(n log n), so it is not the most efficient solution. 
'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t): 
            return False


        dicts = {}
        dictt = {}

        #dictionary: charecter to index. 

        
        for char in s: 
            dicts[char] = dicts.get(char, 0) + 1 # .get alias value to 0 (if not found, return 0)

        for char2 in t: 
            dictt[char2] = dictt.get(char2, 0) + 1

        

        return dicts == dictt 
    
    
    