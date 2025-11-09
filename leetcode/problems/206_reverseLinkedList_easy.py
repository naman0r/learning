# neetcode roadmap linked list

# easy.....

# i lowkey forgot how to do this tho so i watched greg's video. 


'''

for this answer, as well as most linked list answers, there is a recursive approach and an iterative approach we can solve this with.....

lets do the iterative solution first....


two pointers, current and preious...
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        

        curr = head # first element...

        prev = None
        
        while (curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        

        # RECURSIVE SOLUTION


        if not head or not head.next: 
            return head # returns None or head....

        new_head = self.reverseList(head.next)

        # Reverse the current connection
        head.next.next = head
        head.next = None
        
        return new_head



        
        
        


        
        
        

        
        
        