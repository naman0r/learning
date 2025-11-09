# neetcode roadmap sliding window
# 

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


