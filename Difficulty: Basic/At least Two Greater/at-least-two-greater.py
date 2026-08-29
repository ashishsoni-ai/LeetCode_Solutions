class Solution:
    def findElements(self,arr):
        # code here
        arr.sort()
        return arr[:-2]
