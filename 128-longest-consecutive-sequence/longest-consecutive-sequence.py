class Solution:
    def longestConsecutive(self, nums):
        set1 = set(nums)
        max_length = 0

        for num in set1:
            if num - 1 not in set1:
                current = num
                length = 1

                while current + 1 in set1:
                    current += 1
                    length += 1

                
                max_length = max(max_length, length)

        return max_length