# leetcode 75 question #2


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''

        '''

        minprice = float('inf') # +ve infinity as min price

        maxprofit = 0

        for price in prices: 
            minprice = min(minprice, price)

            maxprofit = max(maxprofit, price-minprice)

        return maxprofit


'''
THIS IS THE MOST EFFICIENT SOLUTION.....

- time complexity: o(n)
- space complexity: o(1)

The code loops through the prices list exactly once.

Each operation inside the loop (min, max, subtraction, and assignment) takes constant time, O(1).

So, for n prices, the total time is O(n).


'''