class Solution:
    def findUnique(self, arr):
        # code here 
        xorr = 0
        for num in arr:
            xorr ^= num
        return xorr