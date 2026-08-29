class Solution:
    def remConsonants(self, s):
        # code here
        ans = ""
        allchar = ["a","e","i","o","u","A","E","I","O","U"]
        for char in s:
            if char in allchar:
                ans += char
        return ans