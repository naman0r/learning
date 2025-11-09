# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        

        def nodeEqual(n1, n2):
            if (n1 == None) and (n2 == None): 
                return True

            elif (n1 and n2) and (n1.val == n2.val):
                return nodeEqual(n1.left, n2.left) and nodeEqual(n1.right, n2.right)

            else:
                # one of the nodes do not exist
                return False

            
        return nodeEqual(q, p)