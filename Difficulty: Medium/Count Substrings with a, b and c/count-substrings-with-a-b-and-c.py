class Solution:
    def countSubstring(self, s):
        # Code here
        n = len(s)
        hashmap = {"a":-1,"b":-1,"c":-1}
        count = 0
        for i in range(n):
            hashmap[s[i]] = i
            
            if (hashmap["a"] != -1 and hashmap["b"] != -1 and hashmap["c"] != -1):
                count += 1 + min(
                    hashmap["a"],
                    hashmap["b"],
                    hashmap["c"]
                )
        return count
                
        