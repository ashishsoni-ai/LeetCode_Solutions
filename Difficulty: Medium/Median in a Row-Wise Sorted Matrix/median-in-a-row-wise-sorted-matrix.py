class Solution:
    def median(self, mat):
    	# code here 
    	list1 = []
    	for i in range(len(mat)):
    	    for j in range(len(mat[0])):
    	        list1.append(mat[i][j])
    	list1.sort()        
    	median = len(list1)//2
    	return list1[median]
    	        
    	
    	        