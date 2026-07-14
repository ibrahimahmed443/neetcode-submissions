# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)

        num1, num2 = '', ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        
        sum = str(int(num1) + int(num2))

        # form a linked list with sum
        dummy = ListNode(0)     # dummy node
        l = dummy
        for num in sum:
            l.next = ListNode(num)
            l = l.next
        
        return self.reverseList(dummy.next)

    
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev