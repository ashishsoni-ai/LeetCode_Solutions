class Solution:
	def pushZerosToEnd(self, arr):
    	# code here
    	count = 0
    	for i in range(len(arr)):
    	    if arr[i] != 0:
    	        arr[count],arr[i] = arr[i],arr[count]
    	        count +=1
    	return arr