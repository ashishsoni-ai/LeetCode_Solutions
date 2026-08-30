class Solution:
    def longest(self, arr):
        # code here
        ans = ""
        for char in arr:
            if len(char) > len(ans):
                ans = char
        return ans
            
        