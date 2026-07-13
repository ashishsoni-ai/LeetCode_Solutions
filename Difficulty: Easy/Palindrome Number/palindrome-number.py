class Solution:
    def isPalindrome(self, n):
		# code here
		n = abs(n)
		temp = str(n)
		
		return temp == temp[::-1]
		
		