# medium problem, https://leetcode.com/problems/product-of-array-except-self/description/

'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


'''

# I couldnt do this straightup, had to watch Needcode video on it. I know how to do it in o(n^2) time complexity, 
# but that is not the best way to do it

# also specifies that we cannot use the division operator...


# yeah idk didnt really understand this one. 

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
       
        n = len(nums)
        
        # Step 1: Make a list to store answer
        result = [1] * n

        # Step 2: Go from left to right and multiply all the numbers before each index
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]

        # Step 3: Go from right to left and multiply all the numbers after each index
        right_product = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result
