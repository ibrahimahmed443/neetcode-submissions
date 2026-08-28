# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.indices = {val: i for i, val in enumerate(inorder)}
        self.pre_pos = 0

        def build(low, high):
            if low > high:
                return

            node_val = preorder[self.pre_pos]
            self.pre_pos += 1
            node = TreeNode(node_val)

            mid = self.indices[node_val]
            node.left = build(low, mid - 1)
            node.right = build(mid +1, high)
            return node
        
        return build(0, len(inorder) - 1)




    
    # if not preorder or not inorder:
    #         return None
        
    #     root = TreeNode(preorder[0])
    #     mid = inorder.index(preorder[0])
    #     root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
    #     root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
    #     return root