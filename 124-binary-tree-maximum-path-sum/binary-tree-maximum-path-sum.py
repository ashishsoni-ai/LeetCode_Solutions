# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi = float("-inf")
    def solve(self,root):
        if not root:
            return 0
        LeftSum  = self.solve(root.left)
        if LeftSum < 0:
            LeftSum = 0
        RightSum = self.solve(root.right)
        if RightSum < 0:
            RightSum = 0
        self.maxi = max(self.maxi,LeftSum + RightSum + root.val)
        return root.val + max(RightSum , LeftSum)

    def maxPathSum(self, root: TreeNode | None) -> int:
        self.solve(root)
        return self.maxi
        