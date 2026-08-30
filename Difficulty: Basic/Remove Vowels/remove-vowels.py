class Solution:
	def removeVowels(self, s):
		# code here
		vowel = ["a","e","i","o","u"]
		ans = ""
		
		for char in s:
		    if char not in vowel:
		        ans += char
		return ans
		    
		