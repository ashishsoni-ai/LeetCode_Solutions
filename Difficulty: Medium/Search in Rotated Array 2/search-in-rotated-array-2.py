class Solution:
    def search(self, arr, key):
        # code here
        ans = False
        n = len(arr)
        for i in range(n):
            if arr[i] == key:
                ans = True
        return ans