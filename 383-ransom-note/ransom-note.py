class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        Counter = {}
        for ch in magazine:
            Counter[ch] = Counter.get(ch,0)+1
        for ch in ransomNote:
            if ch not in Counter or Counter[ch] == 0:
                return False
            Counter[ch] -= 1
        return True
        