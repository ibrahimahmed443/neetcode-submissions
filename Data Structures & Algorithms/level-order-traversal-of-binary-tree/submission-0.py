# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        lst = []
        grp_lst = []
        queue = deque()
        queue.appendleft(root)
        
        while len(queue) > 0:
            grp_lst = []
            while len(queue) > 0:
                curr = queue.pop()
                grp_lst.append(curr)
            
            lst.append([node.val for node in grp_lst])

            # queue all nodes at the same level
            for node in grp_lst:
                if node.left: queue.appendleft(node.left)
                if node.right: queue.appendleft(node.right)

        return lst
