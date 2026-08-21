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

        res = []
        grp_lst = []
        queue = deque()
        queue.append(root)
        
        while len(queue) > 0:
            grp_lst = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                grp_lst.append(curr)
            
            res.append([node.val for node in grp_lst])

            # queue all nodes at the same level
            for node in grp_lst:
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return res
