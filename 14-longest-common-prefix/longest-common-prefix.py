class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        ans = ""
        first = strs[0]
        for i in range(len(first)):
            for word in strs[1:]:
                if len(word) == i or word[i] != first[i]:
                    return ans
            ans += first[i]
        return ans




        