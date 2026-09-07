# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def validate(root, lowerBound, upperBound):

            # check if node is not null
            # on node, check if left node is smaller than node self
            # check if right node is bigger than node self
            # if correct, run validate left and right with updated bounds    
        


            # if root is null than automatcially validate
            if not root:
                return True

            if root.val > lowerBound and root.val < upperBound:
                
                return validate(root.left, lowerBound, root.val) and validate(root.right, root.val, upperBound)
            else:
                return False

        return validate(root, float('-inf'), float('inf'))

            

