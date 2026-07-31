class Solution:
	def binaryToDecimal(self, b):
		# code here
		decimal_num = 0
		power = 0
		index = len(b)-1
		while index>=0:
		    num = int(b[index])*(2**power)
		    decimal_num += num
		    power += 1
		    index -= 1
		return decimal_num
		    
		