class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        half = len(candyType)
        total_unique =  len(set(candyType))
        return min(total_unique,half//2)
        