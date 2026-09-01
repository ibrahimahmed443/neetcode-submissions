# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = []

        # create a preorder traversal and add 'N' for null nodes
        # dfs appends to global self.res
        def dfs(node):
            if not node:
                self.res.append('N')
                return
            
            self.res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(self.res)
         
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(',')
        self.i = 0

        # use global index (i) and create tree by advancing the index each time
        def create_node():
            if arr[self.i] == 'N':
                self.i += 1
                return None
            
            node = TreeNode(int(arr[self.i]))
            self.i += 1
            node.left = create_node()
            node.right = create_node()
            return node
        
        return create_node()
