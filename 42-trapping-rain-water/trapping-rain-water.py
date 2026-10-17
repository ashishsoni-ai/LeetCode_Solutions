class Solution:
    def GetMaxLeftArray(self, height, n):
        LeftMax = [0] * n
        LeftMax[0] = height[0]

        for i in range(1, n):
            LeftMax[i] = max(LeftMax[i - 1], height[i])

        return LeftMax

    def GetMaxRightArray(self, height, n):
        RightMax = [0] * n
        RightMax[n - 1] = height[n - 1]

        for i in range(n - 2, -1, -1):
            RightMax[i] = max(RightMax[i + 1], height[i])

        return RightMax

    def trap(self, height: list[int]) -> int:
        n = len(height)

        if n == 0:
            return 0

        LeftMax = self.GetMaxLeftArray(height, n)
        RightMax = self.GetMaxRightArray(height, n)

        total = 0

        for i in range(n):
            h = min(LeftMax[i], RightMax[i]) - height[i]
            total += h

        return total