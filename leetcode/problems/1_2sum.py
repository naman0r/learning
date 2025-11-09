class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        

        '''
        brute force: check every combo of two values
        o(n^2) complexity, which is very inefficient. 
        '''
        
        
        memo ={}

        for i, n in enumerate(nums):
            memo[n] = i
            

        for i, n in enumerate(nums):
            diff = target - n

            if diff in memo and i != memo.get(diff):
                return [i, memo.get(diff)]