class Solution:
    def search(self, arr, key):
        # code here
        ans = -1
        n = len(arr)
        for i in range(n):
            if arr[i] == key:
                ans = i
        return ans
                