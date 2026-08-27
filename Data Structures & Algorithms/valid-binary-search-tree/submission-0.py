# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # start lower and uppoer bounds with -infinity and infinity
        def validate(node, leftBound, rightBound):
            if not node:
                return True

            if not (node.val < rightBound and node.val > leftBound):
                return False
            
            return (validate(node.left, leftBound, node.val) and
            validate(node.right, node.val, rightBound))

        return validate(root, float('-inf'), float('inf'))

