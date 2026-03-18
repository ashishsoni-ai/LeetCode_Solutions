class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n =  len(nums)
        dict1 = {}
        for i in range (n):
            remainder =  target - nums[i]
            if remainder in dict1 :
                return [dict1[remainder],i]   
            dict1[nums[i]] = i
        