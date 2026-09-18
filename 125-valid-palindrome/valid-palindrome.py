class Solution:
    def solve(self,low,high,s):
        if low>=high:
            return True
        if s[low] != s[high]:
            return False
        ans = self.solve(low+1,high-1,s)
        return ans
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ""
        for char in s:
            if char.isalnum():
                new_s += char
        return self.solve(0,len(new_s)-1,new_s)
        