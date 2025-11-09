# Neetcode roadmap for trees

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
        


''' this is not the most efficient solution, since the space compexity is o(n) + o(h), 
    since we are creating a new tree.....
'''
        
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        curr = root

        def helper(current): 
            if current: 
                return TreeNode(current.val, helper(current.right), helper(current.left)) # creating a new tree....

            else: 
                return None # if .right or .left are null, then just return None, the pointer is to None. 


        return helper(root)
    
    
    
    

''' Let's try with the most memory efficient solution.....'''


# the only memory this takes is the recusive stack, so this takes o(h) space......
# no longer wasting memory by creating a new tree and returning that....
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        if not root: 
            return None
        
        left = root.left
        root.left = root.right
        root.right = left

        self.invertTree(root.left)
        self.invertTree(root.right)


        return root