# https://leetcode.com/problems/merge-intervals/
# Solution : https://www.youtube.com/watch?v=2JzRBPFYbKE&t=428s

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        result = []
        intervals.sort(key=lambda x: x[0])
        
        current =intervals[0]
        for interval in intervals:
            if (current[1]>=interval[0]):
                current[1]= max(current[1],interval[1])
            else:
                result.append(current)
                current =interval
        result.append(current)
        return result
        
        
print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge([[1,4],[4,5]]))
print(Solution().merge([[8,10],[9,13]]))
print(Solution().merge([[1,4],[2,3]]))
print(Solution().merge([[1,4],[0,4]]))
print(Solution().merge([[1,4],[0,2],[3,5]]))
print(Solution().merge([[1,4],[0,2],[3,5],[6,7],[8,9],[10,11]]))
print(Solution().merge([[1,4],[0,0]]))
print(Solution().merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
print(Solution().merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]))

'''
[[1,3],[2,6],[8,10],[15,18]]
[[1,4],[4,5]]
[[8,10],[9,13]]
[[1,4],[0,4]]
[[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
[[1,4],[2,3]]
[[2,3],[4,5],[6,7],[8,9],[1,10]]
'''