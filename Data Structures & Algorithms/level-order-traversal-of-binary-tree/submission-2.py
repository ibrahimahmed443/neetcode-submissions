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
                if curr:
                    grp_lst.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            
            if grp_lst:
                res.append(grp_lst)

        return res
