# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root):
        root_val = root.val
        left_val = root.left.val
        right_val = root.right.val
        
        return root_val == (right_val + left_val)