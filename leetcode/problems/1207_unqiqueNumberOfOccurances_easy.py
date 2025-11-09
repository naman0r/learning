# very very easy question..... 

# topics: arrays, hashtable

''' I think this is best time complexity, idk about space complexity tho '''

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        mydict = {} # num to how many occurances it has...

        for num in arr: 
            mydict[num] = mydict.get(num, 0) + 1


        myset = set()

        for occ in mydict.values(): 
            if occ in myset: 
                return False

            else: 
                myset.add(occ)

        
        return True; 
