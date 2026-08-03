class Solution:
    def find(self, l, b, h):
        # code here
        area = 2*(l*b+b*h+h*l)
        volume = l*b*h
        return [area,volume]
        
        