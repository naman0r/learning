# Neetcode roadmap, 2 pointers

# https://leetcode.com/problems/container-with-most-water/description/


'''
o(n) time complexity, o(1) space complexity ??


'''

# Neetcode roadmap, 2 pointers

# https://leetcode.com/problems/container-with-most-water/description/


'''
o(n) time complexity, o(1) space complexity ??


'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        maxArea = 0
        

        l = 0
        r = len(height) - 1
        
        while l < r : 
            volume = min(height[l], height[r]) * (r - l)
            maxArea = max(volume, maxArea) # checking max between the two
            
            if height[r] > height[l]: 
                # want to keep right height, so increment left
                l+=1

            else: 
                r-=1

        return maxArea
            

            
        
            

            
        