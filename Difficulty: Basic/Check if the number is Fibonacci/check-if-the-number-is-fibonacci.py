class Solution:
    def isFibonacci(self, n):
        a = 0
        b = 1
        
        while a < n:
            a, b = b, a + b
        
        if a == n:
            return True
        else:
            return False