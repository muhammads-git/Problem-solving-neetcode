# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # cold coding

        """ 
        curr = head
        - go for the whole lisst and fidn the Length
        - theres formula L-n = r 
        - the r will be the steps to be takn to reach the prev node of nth.
        [1,3,4,5,4] = n = 3
        5 - 3 = 2 .. we need to take two steps to reach the prevoud node of the nth
        prev.next = prev.next.next

        [2] 
        dummy = ListNode()
        dummy.next = head
        curr 
        for steps:
            prev =prev.next
        prev.next = prev.next.next

        return dummy.next
        """

        dummy = ListNode()

        dummy.next = head
        prev = dummy
        curr = head

        L = 0
        steps = 0

        while curr is not None:
            curr = curr.next
            L = L + 1

        steps = L - n

        for i in range(steps):
            prev= prev.next
        
        prev.next = prev.next.next

        return dummy.next

            

