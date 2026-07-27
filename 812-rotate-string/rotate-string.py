class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        curr_s = s
        if len(s) != len(goal):
            return False
        n = len(curr_s)

        for i in range(n):
            if curr_s == goal :
                return True
            curr_s = curr_s[-1] + curr_s[:-1]

        return False
        