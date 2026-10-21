class Solution:
    def activitySelection(self, start: list[int], finish: list[int]) -> int:
        
        n = len(start)
        meet = []
        for i in range(n):
            meet.append([start[i],finish[i]])
            
        meet.sort(key = lambda x:x[1])
        count = 1
        lastMeet = meet[0][1]
        
        for i in range(1,n):
            if meet[i][0] > lastMeet:
                count += 1
                lastMeet = meet[i][1] 
        return count
                