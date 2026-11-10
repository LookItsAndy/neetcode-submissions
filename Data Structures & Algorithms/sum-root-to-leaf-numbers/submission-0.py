# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        string_int_list = []
        string_int = ""
        total = 0

        def traverse(root, string_int):

            if root:
                string_int += str(root.val)

                if root.left:
                    traverse(root.left, string_int)
                if root.right:
                    traverse(root.right, string_int)

                elif root.left == None and root.right == None:   # if there is root is null, then reached leaf so add completed string to string_int_list
                    string_int_list.append(string_int)
                    print(string_int_list)


            return string_int


        traverse(root, string_int)

        for val in string_int_list:
            total += int(val)


        return total