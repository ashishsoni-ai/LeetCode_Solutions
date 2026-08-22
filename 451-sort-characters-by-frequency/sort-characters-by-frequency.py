class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ""
        hashmap = {}
        for ch in s:
            hashmap[ch] = hashmap.get(ch,0) + 1
        sorted_char = sorted(hashmap.items(),key = lambda x:x[1],reverse= True)
        for ch,freq in sorted_char:
            ans = ans+(ch*freq)
        return ans
        