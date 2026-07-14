# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = '', ''
        while l1 or l2:
            if l1:
                s1 += str(l1.val)
                l1 = l1.next
            if l2:
                s2 += str(l2.val)
                l2 = l2.next

        sum = str(int(s1[::-1]) + int(s2[::-1]))

        dummy = ListNode(0)
        l = dummy
        for num in sum[::-1]:
            l.next = ListNode(num)
            l = l.next

        return dummy.next
