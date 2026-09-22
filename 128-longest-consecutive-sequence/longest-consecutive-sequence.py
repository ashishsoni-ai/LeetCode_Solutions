class Solution:
    def FindLnegth(self,key,mp):

        ans = 0
        while key in mp:
            ans += 1
            key += 1
        return ans


    def longestConsecutive(self, nums: list[int]) -> int:
        mp  = {}
        max_length = 0
        for i in range(len(nums)):
            mp[nums[i]] = True

        for j in range(len(nums)):
            if nums[j]-1 in mp:
                mp[nums[j]] = False

        for key in mp:
            if mp[key] == True:
                max_length = max(max_length,self.FindLnegth(key,mp))
        return max_length


        