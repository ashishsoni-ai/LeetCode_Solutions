class Solution:
    def thirdLargest(self,arr):
        # code here
        arr.sort()
        if len(arr)<3:
            return -1
        return arr[-3]
        