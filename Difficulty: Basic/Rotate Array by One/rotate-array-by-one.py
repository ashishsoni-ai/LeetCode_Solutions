class Solution:
    def rotate(self, arr):
        n = len(arr)
        arr[:] = [arr[-1]]+arr[0:n-1]
        return arr
    
