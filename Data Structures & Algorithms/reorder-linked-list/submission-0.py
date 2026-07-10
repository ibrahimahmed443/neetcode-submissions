# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle of the list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None

        # reverse 2nd half
        prev = None
        while second_half:
            next = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = next
        
        second_half = prev          # last non None value

        # merge two halves
        first_half = head
        while second_half:
            tmp1 = first_half.next
            tmp2 = second_half.next
            first_half.next = second_half
            second_half.next = tmp1

            first_half = tmp1
            second_half = tmp2
            
       