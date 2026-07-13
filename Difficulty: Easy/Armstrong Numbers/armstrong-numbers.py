class Solution:
    def armstrongNumber (self, n):
        # code here 
        temp = n
        add = 0
        while n != 0:
            single_digit = n%10
            add += (single_digit)**3
            n = n//10
        if temp == add:
            return True
        else:
            return False
            