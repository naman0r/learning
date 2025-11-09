# Medium question
# https://leetcode.com/problems/top-k-frequent-elements/description/


n = 10
freq = [[] for _ in range(n)]
print(freq)
# An array with 10 empty arrays. 




'''

THis is an o(n) time solution for this problem. 
I brute forced it but it was very inefficient. I got this solution after wathcing the neetcode video. 
COME BACK AT SOME POINT, NOT UNDERSTOOD PROPERLY. 
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # seems like a dictionary question

        count = {}
        freq = [[] for i in range(len(nums) + 1)]


        
        for num in nums: 
            count[num] = count.get(num, 0) + 1

        # return key, value pairs 
        for n,c in count.items(): 
            # at at index 2 of frequency, the correspoding array is the array of 
            # numbers that occurerd exactly 2 times in the input nums array. 
            freq[c].append(n) # this is why we can use the append method.....
            


        res = []
        # from the last index of freq, until 0, decrementing by -1 every time....
        for i in range (len(freq) - 1, 0, -1 ): 
            # for every number that occurs `i` times.....
            for n in freq[i]: 
                res.append(n)
                if (len(res) == k): 
                    return res
                


        
        

        