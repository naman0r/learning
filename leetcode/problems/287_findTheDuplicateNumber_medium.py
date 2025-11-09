# this is a suspicously easy question... why is this supposed to be hard? 



''' This solution is o(n) tc and o(n) sc. optimal solution has o(1) sc. '''
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        myset = set()

        for num in nums: 
            if num not in myset: 
                myset.add(num)

            else: 
                return num



''' Trying for the optimal solution with o(n) tc and o(1) sc.....'''

# * this is a hard problem, need to come back later....