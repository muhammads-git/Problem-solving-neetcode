# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwosortedList(l1:List[ListNode], l2:List[ListNode]):
            dummy = ListNode()
            curr = dummy

            while l1 and l2:
                if l1 is not None and l2 is not None:
                    if l1.val < l2.val:
                        curr.next = l1
                        curr = curr.next
                        l1 = l1.next
                    elif l1.val > l2.val:
                        curr.next = l2
                        curr = curr.next
                        l2 = l2.next
                    else:
                        curr.next = l1
                        curr = curr.next
                        l1 = l1.next

            curr.next = l1 or l2
            # curr = curr.next
            return dummy.next

        # base cases
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        # split
        mid = len(lists) // 2
        left = lists[:mid]
        right = lists[mid:]

        left_merged = self.mergeKLists(left)
        right_merged = self.mergeKLists(right)

        return mergeTwosortedList(left_merged, right_merged)
            
                    
