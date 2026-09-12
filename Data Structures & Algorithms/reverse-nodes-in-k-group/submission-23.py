# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        prev = dummy

        while True:
            curr = head

            for i in range(k):
                if curr is None:
                    return dummy.next
                curr = curr.next

            #
            group_head = head
            prev_node = None
            tail=head

            for i in range(k):
                nxt = group_head.next
                group_head.next = prev_node
                prev_node = group_head
                group_head = nxt
                
          
            #
            prev.next = prev_node
            tail.next = curr
            prev = tail
            head = curr
