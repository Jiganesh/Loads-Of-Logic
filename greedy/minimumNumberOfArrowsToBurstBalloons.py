#https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        points.sort(key=lambda x: x[1])
        
        prev=points[0][1]
        res=0
        
        for i in points:
            if (i[0]>prev): res+=1;  prev= i[1];
        return res+1
    

print(Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(Solution().findMinArrowShots([[[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]]))

