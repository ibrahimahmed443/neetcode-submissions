import copy
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# brute force solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(curr, prev):
            if not curr:
                return prev
            
            next = curr.next
            curr.next = prev
            return reverse(next, curr)

        return reverse(head, None)