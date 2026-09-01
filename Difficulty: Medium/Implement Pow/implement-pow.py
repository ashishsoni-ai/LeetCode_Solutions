class Solution:
    def power(self, b: float, e: int) -> float:
        # Code Here
        if e == 0:
            return 1.00000
        if e == 1:
            return b
        if e < 0:
            b = 1/b
            e = -e
        if e % 2 == 0:
            return self.power(b*b,e//2)
        return b*self.power(b,e-1)