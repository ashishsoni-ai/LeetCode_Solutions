class Solution:
    def maxProduct(self, nums):
        curr_max = nums[0]
        curr_min = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            # Save old values before updating
            temp_max = curr_max
            temp_min = curr_min

            curr_max = max(x, x * temp_max, x * temp_min)
            curr_min = min(x, x * temp_max, x * temp_min)

            ans = max(ans, curr_max)

        return ans
        