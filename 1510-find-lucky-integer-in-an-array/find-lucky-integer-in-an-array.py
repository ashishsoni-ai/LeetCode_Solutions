class Solution:
    def findLucky(self, arr):
        freq = {}

        # Count frequency
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        ans = -1

        # Check lucky integers
        for key in freq:
            if key == freq[key]:
                ans = max(ans, key)

        return ans