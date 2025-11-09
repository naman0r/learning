## neetcode roadmap in binary search category



class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # bineary search is meant to have an O(log n) time complexity. 

        # this is the recursice approach, not changing the array itself. 

        def binary_search(l, r, nums):
            '''
            l : left [int]
            r : right [int]
            nums : number array [array int]
            '''

            # base case: 
            if l > r: 
                return -1
            
            m = l + ((r - l) // 2) # forcing result into an integer

            if nums[m] < target: 
                return binary_search(m + 1,r, nums)
            
            elif nums[m] > target: 
                return binary_search(l, m -1, nums)
            else: # nums[m] == target: 
                return m

        
        return binary_search(0, len(nums) - 1, nums)


        