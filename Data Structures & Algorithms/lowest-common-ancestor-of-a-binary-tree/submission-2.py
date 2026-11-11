# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # need to locate p and q

        # keep note of what nodes were visited before seeing the first p or q.

        # notice: if p is in the subtree of q, then q is the LCA, vice versa

        p_path = []
        q_path = []


        def traverse(root, path):
            nonlocal p_path, q_path
            if root:
                path.append(root)   # add element to the path
            
                if root is p:       # check if p was found and record the path
                    p_path = path.copy()
                if root is q:     # check if q was found and record the path
                    q_path = path.copy()
                                  # otherwise, continue building path
                traverse(root.left, path)
                traverse(root.right, path)
                path.pop()


        traverse(root, [])

        matching_prev = None
        for i in range(min(len(p_path),len(q_path))):
            if p_path[i] is q_path[i]:
                matching_prev = p_path[i]
            else:
                break

        return matching_prev
                
