class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        set1 = set(nums)
        max_length = 0
        for num in set1:
            if num-1 not in set1:
                curr = num
                length = 1
                while curr+1 in set1:
                    curr += 1
                    length += 1
                max_length = max(max_length,length)
        return max_length
        