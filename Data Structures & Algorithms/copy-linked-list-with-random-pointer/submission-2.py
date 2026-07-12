"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        currToCopyMap = {}

        curr = head
        while curr:
            copy = Node(curr.val)
            currToCopyMap[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = currToCopyMap[curr]
            copy.next = currToCopyMap.get(curr.next, None)
            copy.random = currToCopyMap.get(curr.random, None)
            curr = curr.next
        
        return currToCopyMap.get(head)
