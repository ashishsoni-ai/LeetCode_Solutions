class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        s.sort()
        g.sort()
        g_len = len(g)
        s_len = len(s)
        left = 0
        right = 0
        count = 0
        while left < g_len and right < s_len:
            if g[left] <= s[right]:
                count += 1
                left += 1
            right += 1
        return count
    
        