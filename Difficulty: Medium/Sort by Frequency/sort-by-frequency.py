class Solution:
    def frequencySort(self, s):
        # code here
        ans = ""
        hashmap = {}
        for char in s:
            hashmap[char] = hashmap.get(char,0)+1
        sorted_char = sorted(hashmap.items(),key = lambda x:(x[1],x[0]))
        for char,freq in sorted_char:
            ans = ans + (char*freq)
        return ans
            
            
            