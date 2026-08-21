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
            q_len = len(queue)
            for _ in range(q_len):
                curr = queue.popleft()
                grp_lst.append(curr.val)
                
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            
            res.append(grp_lst)

        return res
