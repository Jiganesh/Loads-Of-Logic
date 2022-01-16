# https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution(object):
    
    # Runtime: 24 ms, faster than 100.00% of Python online submissions for Minimum Moves to Reach Target Score.
    # Memory Usage: 13.3 MB, less than 100.00% of Python online submissions for Minimum Moves to Reach Target Score.
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        count =0
        while target >1 and maxDoubles:
            if maxDoubles and target%2==0 and target//2 >=1:
                target=target//2
                maxDoubles-=1
            else:
                target-=1
            count+=1
        return (count+target-1)
    
    
            
    
print(Solution().minMoves(target=5, maxDoubles=0)) # 4
print(Solution().minMoves(target=19, maxDoubles=2)) # 7
print(Solution().minMoves(target=10, maxDoubles=5)) # 4
print(Solution().minMoves(target=656101987, maxDoubles=1)) # 328050994