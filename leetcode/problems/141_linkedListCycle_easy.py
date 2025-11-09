# neetcode roadmap for Linked Lists....

# pretty easy question, i think that this is the most efficient possible solution....


'''
time complexity is o(n) and space complexity is o(n). the most efficient solution is technocallu
o(1) space complexity, but I also implemented that here (2 pointer approach i think)
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """


        # set of ListNodes? 

        myset = set()
        

        while head:
            if head in myset: 
                return True
            else: 
                myset.add(head)
                head = head.next


            
        # if at one point head.next is null, then there is no cycle
        # case #1
        return False
        
        
        
        
''' 2 POINTER APPROACH: MOST OPTIMAL!!! '''
        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """


        # o(n) space = hashset approach
        # 2 pointer approach = o(1) space complexity (most efficient)
        # best case time complexity is o(n)


        if not head or not head.next: 
            return False # first edge case....


        fast = head
        slow = head 

        # logic -> p1 increment by 1, p2 increment by 2. 
        # if p1 == p2 at any point, then return true. 
        # if either p1 or p2 ever become null, then return false. 

        while fast and fast.next: 

            slow = slow.next
            fast = fast.next.next

            if slow == fast: 
                return True


        return False

        