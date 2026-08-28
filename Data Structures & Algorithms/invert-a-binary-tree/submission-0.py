# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # intuition: recursively iterate through the tree. at each node, invert the left and right. then run again through the left subtree and right subtree. continue until node points to None

        # new tree
        
        def invert(root):

            if root:
                root.left, root.right = root.right, root.left
                invert(root.left)
                invert(root.right)
            return root

        return invert(root)

