class Solution:
    def leaders(self, arr):
        # code here
        ans = []
        max_element = float("-inf")
        n = len(arr)
        for i in range(n-1,-1,-1):
            
            if arr[i] >= max_element:
                max_element = arr[i]
                ans.append(max_element)
                
        return ans[::-1]
                
                