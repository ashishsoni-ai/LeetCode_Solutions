class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        ans = ""
        for char in s:
            if char == "(":
                count += 1
                if count > 1:
                    ans += char
            else:
                count -= 1
                if count>0:
                    ans += char
        return ans
                



        
        