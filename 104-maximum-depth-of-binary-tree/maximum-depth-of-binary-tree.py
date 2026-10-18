# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root):
        if root == None:
            return 0
        LeftHeight = self.solve(root.left)
        RightHeight = self.solve(root.right)

        return 1 + max(LeftHeight,RightHeight)
    def maxDepth(self, root: TreeNode | None) -> int:
        return self.solve(root)


        