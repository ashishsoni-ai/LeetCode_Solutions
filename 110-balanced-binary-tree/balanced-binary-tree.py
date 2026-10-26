# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root):
        if root is None:
            return 0
        LeftHeight = self.solve(root.left)
        if LeftHeight == -1:
            return -1
        RightHeight = self.solve(root.right)
        if RightHeight == -1:
            return -1
        
        if abs(LeftHeight-RightHeight) > 1:
            return -1
        return 1 + max(LeftHeight,RightHeight)

    def isBalanced(self, root: TreeNode | None) -> bool:
        ans = self.solve(root)
        if ans == -1:
            return False
        return True

        