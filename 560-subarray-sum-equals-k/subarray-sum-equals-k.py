class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict1 = {0:1}
        curr_sum = 0
        count = 0
        for num in nums:
            curr_sum += num
            required = curr_sum - k
            if required in dict1:
                count += dict1[required]
            if curr_sum not in dict1:
                dict1[curr_sum] = 1
            else:
                dict1[curr_sum] += 1
        return count

