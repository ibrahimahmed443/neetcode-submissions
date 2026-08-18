# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (q and not p):
            return False

        stack1 = [p]
        stack2 = [q]
        while stack1 or stack2:
            curr1, curr2 = stack1.pop(), stack2.pop()
            if curr1.val != curr2.val:
                return False
            
            if curr1.left == None and curr2.left != None:
                return False
            
            if curr1.right == None and curr2.right != None:
                return False

            if curr1.right: stack1.append(curr1.right)
            if curr1.left: stack1.append(curr1.left)

            if curr2.right: stack2.append(curr2.right)
            if curr2.left: stack2.append(curr2.left)
        
        return len(stack1) == len(stack2)

        