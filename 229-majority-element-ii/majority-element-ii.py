class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        count1 = 0
        count2 = 0

        majority_element1 = None
        majority_element2 = None

        ans = []

        # Find two possible candidates
        for i in range(n):

            if nums[i] == majority_element1:
                count1 += 1

            elif nums[i] == majority_element2:
                count2 += 1

            elif count1 == 0:
                majority_element1 = nums[i]
                count1 = 1

            elif count2 == 0:
                majority_element2 = nums[i]
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1

        # Verification
        freq1 = 0
        freq2 = 0

        for num in nums:
            if num == majority_element1:
                freq1 += 1

            elif num == majority_element2:
                freq2 += 1

        if freq1 > n // 3:
            ans.append(majority_element1)

        if freq2 > n // 3:
            ans.append(majority_element2)

        return ans