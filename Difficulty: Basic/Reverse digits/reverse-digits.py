class Solution:
	def reverseDigits(self, n):
		# Code here
		ans = 0
		while n>0:
		    temp = n%10
		    ans = ans*10 + temp
		    n = n//10
		return ans
		    