class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        freq = {}
        # Step 1:- Count frequency
        for num in nums:
            freq[num] = freq.get(num,0)+1
        # Step 2:- Find first unique even
        for num in nums:
            if num%2==0 and freq[num] == 1:
                return num
        return -1
        