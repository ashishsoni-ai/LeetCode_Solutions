class Solution:
    def maxDepth(self, s):
        # code here
        count = 0
        max_depth = 0
        for bracket in s:
            if bracket == "(":
                count += 1
                max_depth = max(count,max_depth)
            elif bracket == ")":
                count -= 1
        return max_depth
        