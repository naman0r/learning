# leetcode 75 question #5. Easy level difficulty. 

'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.
'''

# Apparently using something called fucking Kadane’s Algorithm ??????



# this is a pretty easy question, just need to think through the questions before solving them...
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        # have two numbers, one for tracking current sum,
        # and one for the max so far. 

        max_sum = float('-inf')
        current = 0; 
        
        for num in nums: 
            current = max(num, current + num)

            max_sum = max (current, max_sum)

        
        return max_sum
            

        