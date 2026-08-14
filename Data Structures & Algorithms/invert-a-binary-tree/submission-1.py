# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return root
        
        queue = deque()
        queue.appendleft(root)

        while len(queue) > 0:
            curr = queue.pop()

            curr.left, curr.right = curr.right, curr.left

            if curr.left: queue.appendleft(curr.left)
            if curr.right: queue.appendleft(curr.right)
        
        return root

        # print(self.dfs(root))
        # print(self.dfs_iterative(root))
        # print(self.bfs(root))

    # def dfs(self, root):
    #     if not root:
    #         return []
        
    #     left = self.dfs(root.left)
    #     right = self.dfs(root.right)
    #     return [root.val, *left, *right]

    # def dfs_iterative(self, root):
    #     result = []
    #     if not root:
    #         return result
        
    #     stack = [root]
    #     while len(stack) > 0:
    #         curr = stack.pop()
    #         result.append(curr.val)

    #         if curr.right: stack.append(curr.right)
    #         if curr.left: stack.append(curr.left)
        
    #     return result

    # def bfs(self, root):
    #     result = []
    #     if not root:
    #         return result
        
    #     queue = deque()
    #     queue.appendleft(root)

    #     while len(queue) > 0:
    #         curr = queue.pop()
    #         result.append(curr.val)

    #         if curr.left: queue.appendleft(curr.left)
    #         if curr.right: queue.appendleft(curr.right)
        
    #     return result

