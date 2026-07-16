class Solution:
    def mostFreqEle(self, arr):
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        max_freq = 0
        ans = -1

        for key, value in freq.items():
            if value > max_freq:
                max_freq = value
                ans = key
            elif value == max_freq and key > ans:
                ans = key

        return ans