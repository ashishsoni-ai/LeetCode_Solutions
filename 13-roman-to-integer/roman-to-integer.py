class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        dict1 = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        Count = 0
        for i in range(n):
            if i<n-1 and dict1[s[i]]<dict1[s[i+1]]:
                Count -= dict1[s[i]]
            else:
                Count += dict1[s[i]]
        return Count
        