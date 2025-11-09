## neetcode roadmap, binary search....

# this is kinda hard ngl

# watched neetcode video https://www.youtube.com/watch?v=U2SozAs9RzA&t=326s

# brute force solution, start at k = 1 and count upwards and check if it works....

# oh.... max number of piles is max(piles)


class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
    
        # bannanas per hour = k; which we need to return


        # h hours, k speed. s

        # koko can only eat at most one entire pile of banaas in an hour. 

        # max k is max(piles)

        # min k is 1....
        # 2 pointers approach on k.......
  


        import math

        left = 1
        right  = max(piles)

        result = right


        while left <= right: 
            k = (left + right) // 2
            hours = 0

            for pile in piles: 
                hours += math.ceil(float(pile) / k) # not putting float here was breaking the code
                # i am literally so confused. 
                

            if (hours <= h):
                result = k
                # this means we went too fast, so we can slow down 
                right = k - 1

            else: 
                left = k + 1

        
        return result 
        
                