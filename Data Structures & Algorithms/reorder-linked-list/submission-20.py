# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        fast,slow = head.next,head
        curr = head


        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # slow is on the midd
        right = slow.next
        slow.next = None

        # reverse the right
        prev = None
        curr = right
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        right = prev
        left = head
        dummy = ListNode()
        curr_dummy = dummy
        # merge into dummy
        while left and right:
            nxt_left = left.next
            nxt_right = right.next

            left.next = right
            right.next = nxt_left

            # increment left and right pointers
            left = nxt_left
            right =nxt_right

        # curr_dummy.next = left or right
        # curr_dummy = curr_dummy.next

        return dummy.next


