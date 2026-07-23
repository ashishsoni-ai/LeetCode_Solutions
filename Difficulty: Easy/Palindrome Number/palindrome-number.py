class Solution:
    def isPalindrome(self, n):
		# code here
		n = abs(n)
		replica = abs(n)
		ans = 0
		if -9<=n<=9:
		    return True
		while replica>0:
		    temp = replica%10
		    ans = ans*10+temp
		    replica = replica//10
		if ans == n:
		    return True
		return False
		    