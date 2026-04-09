class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints)
        left_sum = 0
        right_sum = 0
        max_point = 0
        for i in range(0,k):
            left_sum += cardPoints[i]
        max_point = left_sum
        right_end = len(cardPoints)-1
        for i in range(k-1,-1,-1):
            left_sum -= cardPoints[i]
            right_sum += cardPoints[right_end]
            max_point = max(max_point,right_sum+left_sum)
            right_end -= 1

        return max_point

