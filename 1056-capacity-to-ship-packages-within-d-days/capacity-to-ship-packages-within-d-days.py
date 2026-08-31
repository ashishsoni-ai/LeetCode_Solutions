class Solution:
    def shipWithinDays(self, weights, d):
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2

            # Calculate days needed for this capacity
            daysNeeded = 1
            currentLoad = 0

            for weight in weights:
                if currentLoad + weight > mid:
                    daysNeeded += 1
                    currentLoad = weight
                else:
                    currentLoad += weight

            # Check if this capacity is enough
            if daysNeeded <= d:
                right = mid
            else:
                left = mid + 1

        return left