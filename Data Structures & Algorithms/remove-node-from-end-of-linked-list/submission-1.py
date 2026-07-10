# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        tail = head
        while tail:
            length += 1
            tail = tail.next
        
        m = length - n      # m = position from start
        prev = None
        curr = head
        i = 0
        print(m)
        while curr:
            if m == i:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next    # remove from 0 index and move head forward
                break

            prev = curr
            curr = curr.next
            i += 1
        
        return head
