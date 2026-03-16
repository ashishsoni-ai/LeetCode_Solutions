class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = len(s.strip().split()[-1])
        return word
        

        