# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next=head
        fast=head
        slow=dummy
        # [1,2,3,4]
        for i in range(n):
            fast=fast.next
        # fast=ON2
        # slow=dummy
        while fast is not None:
            fast=fast.next
            slow=slow.next
        
        slow.next=slow.next.next
        slow=slow.next
        return dummy.next
            