# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# brute force solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        new_list = dummy

        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        while arr:
            new_list.next = ListNode(arr.pop())
            new_list = new_list.next
        
        return dummy.next
