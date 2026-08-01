# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        # cold recall this reverse linked list in a minute
        # then go ahead for another problem...

        curr = head
        prev = None

        while curr is not None:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt
        return prev