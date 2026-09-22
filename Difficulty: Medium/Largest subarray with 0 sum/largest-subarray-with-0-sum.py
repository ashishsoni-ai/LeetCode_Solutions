class Solution:
    def maxLength(self, arr):
        mp = {}
        max_len = 0
        total = 0
        i = -1
        mp[total] = i
        
        while i < len(arr)-1:
            i += 1
            total += arr[i]
            if total not in mp:
                mp[total] = i
            else:
                length = i - mp[total]
                if max_len < length :
                    max_len = length
        return max_len
        
        