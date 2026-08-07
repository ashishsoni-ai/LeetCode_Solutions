class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n <=0:
        #     return False
        # while n%2 == 0:
        #     n = n//2
        # if n == 1:
        #     return True
        # else:
        #     return False
        # if n<=0 :
        #     return False
        # if n==1:
        #     return True
        # if n%2!=0:
        #     return False
        # #recursive
        # return self.isPowerOfTwo(n//2)

        if n == 0:
            return False
        return (n&n-1) == 0

       