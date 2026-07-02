class Solution:
    def largest(self, arr):
        # code here
        big = arr[0]
        l = len(arr)
        for i in range(l):
            if arr[i] > big:
                big = arr[i]
        return big
