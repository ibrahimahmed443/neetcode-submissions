# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = root.val

        # return max path sum without split
        def dfs(node):
            if not node:
                return 0
            
            leftSum = max(dfs(node.left), 0)
            rightSum = max(dfs(node.right), 0)

            # update max path sum with split
            self.maxSum = max(self.maxSum, node.val + leftSum + rightSum)

            return node.val + max(leftSum, rightSum)
        
        dfs(root)
        return self.maxSum
