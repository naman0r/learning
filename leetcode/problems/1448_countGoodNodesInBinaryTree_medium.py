# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """


        # traverse the whole tree.....

        def countGood(node, max):

            if not node: 
                return 0

            elif node.val > max: 
                return 1 + countGood(node.left, node.val) + countGood(node.right, node.val)

            else: # meaning that node is not 'good'
                return countGood(node.left, max) + countGood(node.right, max)


        # we can also do 
        # return countGood(root.left, root.val) + countGood(root.right, root,val)

        return countGood(root, float('-inf'))



        