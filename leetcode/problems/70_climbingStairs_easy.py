# memoization question.....

# first Dynamic Programming question....


''' this is the most efficient time complexity solution....

can be o(1) spcace complexity but ceebs
'''


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # climber can climb either 1 or 2 steps at a time.....

        memo = {}



        def helper(steps):
            if steps in memo: 
                return memo[steps]

            elif steps <= 2: 
                return steps; 

            else: 
                memo[steps] = helper(steps - 1) + helper(steps - 2)
                return memo[steps]

        

        return helper(n)

        