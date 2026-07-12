class Solution:
    def twoSum(self, arr, target):
        set1 = set()

        for num in arr:
            complement = target - num

            if complement in set1:
                return True

            set1.add(num)

        return False