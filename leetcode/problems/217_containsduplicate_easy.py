# leetcode 75 question #3


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()

        for num in nums: 
            if num not in seen: 
                seen.add(num)
            else : 
                return True

        
        return False; 


'''
- time complexity: o(n)
- space complexity: o(n)

The code loops through the nums list exactly once.

Each operation inside the loop (add, check, and assignment) takes constant time, O(1).

So, for n numbers, the total time is O(n).


LIST IS NOT EFFICIENT SINCE LIST LOOKUPS ARE o(N) time COMPLEXITY WHEREAS SET LOOKUPS ARE o(1) time COMPLEXITY.

'''


class SolutionNotOptimalTimedOut(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = []

        for num in nums: 
            if num not in seen: 
                seen.append(num)
            else : 
                return True

        
        return False; 



        