# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # use depth first search

        def depth (root, currDepth):

            if root: 
                currDepth += 1
                leftDepth = depth(root.left, currDepth)
                rightDepth = depth(root.right, currDepth)
                return max(leftDepth, rightDepth)
            return currDepth
                


        return depth(root, 0)