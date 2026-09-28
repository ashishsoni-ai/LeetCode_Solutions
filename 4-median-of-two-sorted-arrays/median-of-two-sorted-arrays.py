class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        nums3 = nums1 + nums2
        nums3.sort()

        n = len(nums3)

        if n % 2 != 0:
            return nums3[n // 2]

        else:
            mid1 = n // 2 - 1
            mid2 = n // 2

            return (nums3[mid1] + nums3[mid2]) / 2

        