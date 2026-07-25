# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged_list = ListNode()
        if len(lists) == 0:
            return merged_list.next
        
        for i, list in enumerate(lists):
            if i == 0:
                merged_list = list
            else:
                merged_list = self.mergeTwoLists(merged_list, list)
        
        return merged_list

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode
        merged_list = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                merged_list.next = list1
                list1 = list1.next
            else:
                merged_list.next = list2
                list2 = list2.next
            merged_list = merged_list.next
        
        if list1:
            merged_list.next = list1
        else:
            merged_list.next = list2
        
        return dummy.next