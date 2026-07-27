class Solution:
    def areRotations(self, s1, s2):
        # code here
        if len(s1) != len(s2):
            return False
        double_s = s1 + s1
        
        if s2 in double_s:
            return True
        return False
            