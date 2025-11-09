# neetcode roadmap, stack

# https://leetcode.com/problems/min-stack/description/

'''
This is a really interesting, kind of system design problem.
'''

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """

        self.stack.append(val)


        # if there is a minStack, see what is the current minimum
        if self.minStack: 
            val = min(val, self.minStack[-1]) # [-1] index is the last element


        # if there is no minstack, then essentially add this since it is the min val.....
        self.minStack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """

        self.stack.pop()
        self.minStack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()