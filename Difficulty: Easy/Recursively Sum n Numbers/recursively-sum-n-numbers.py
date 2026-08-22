class Solution:
    def recursiveSum(self, n):
        # code here
        if n == 1:
            return 1
        if n<=0:
            return 0
        return n +self.recursiveSum(n-1)
        