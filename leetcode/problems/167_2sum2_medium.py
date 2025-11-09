# Neetcode roadmap for two pointers

# i did this with no problem, did not use any help!! but this is a really easy question...



'''
o(n) time complexity, o(1) space complexity. 
'''

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # since this is a sorted array, we should be able to do this in a more efficient manner than o(n)

        l = 0
        r = len(numbers) - 1

        while l < r: 
            # means that sum is too large, so decrement the right pointer
            if (numbers[l] + numbers[r] > target): 
                r -=1; 
                continue
            elif (numbers[l] + numbers[r] < target): 
                l +=1; 
                continue

            else: # else has to mean that the sum adds up....
                return [l + 1, r + 1] 
        