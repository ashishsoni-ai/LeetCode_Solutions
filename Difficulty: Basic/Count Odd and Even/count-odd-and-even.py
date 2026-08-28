class Solution:
	def countOddEven(self, arr):
		#Code here
		evencount = 0
		oddcount = 0
		for i in range(len(arr)):
		    if arr[i]%2 == 0:
		        evencount += 1
		    else:
		        
		        oddcount += 1
		return oddcount,evencount
		  
		