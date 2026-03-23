class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = s.lower()
        # t = t.lower()
        # count = [0]*26
        # if len(s) != len(t):
        #     return False
        # for word in s:
        #     count[ord(word)-ord('a')] += 1
        # for word in t:
        #     count[ord(word)-ord('a')] -= 1
        # for num in count:
        #     if num != 0:
        #         return False
        # return True 
        list1 = list(s)
        list2 = list(t)
        list1.sort()
        list2.sort()
        if list1 == list2:
            return True
        else:
            return False


        