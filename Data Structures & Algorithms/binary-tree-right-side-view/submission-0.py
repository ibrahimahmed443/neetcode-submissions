# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()
        q.append(root)
        res = []

        while q:
            grp_list = []
            q_len = len(q)
            for _ in range(q_len):
                curr = q.popleft()
                grp_list.append(curr.val)

                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)

            res.append(grp_list.pop())
        
        return res
