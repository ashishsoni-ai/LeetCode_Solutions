class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        i = len(s)-1
        vowel = {'a','e','i','o','u'}
        while i>=0 and s[i] in vowel:
            i -= 1
        return s[0:i+1]