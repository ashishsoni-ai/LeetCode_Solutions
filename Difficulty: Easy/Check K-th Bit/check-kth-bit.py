class Solution:
    def checkKthBit(self, n, k):
        return ((n >> k) & 1) == 1
        