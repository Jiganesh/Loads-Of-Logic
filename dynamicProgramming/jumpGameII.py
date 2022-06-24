# https://leetcode.com/problems/jump-game-ii/
# https://www.youtube.com/watch?v=dJ7sWiOoK7g&t=370s


class Solution:
    
    # Runtime: 15176 ms, faster than 5.00% of Python3 online submissions for Jump Game II.
    # Memory Usage: 31.6 MB, less than 5.00% of Python3 online submissions for Jump Game II.
    
    def jump(self, nums) -> int:
        dp = {}
        
        def helper( index = 0):
            if index >= len(nums)-1:
                return 0
            
            if index in dp :
                return dp[index]
            
            ans = float('inf')
            for i in range (index+1 , index +nums[index]+1):
                ans = min(ans, 1+helper(i))
            dp[index]= ans
            return ans
        
        index=0
        return helper(index)
    
    # Runtime: 139 ms, faster than 89.06% of Python3 online submissions for Jump Game II.
    # Memory Usage: 15.1 MB, less than 23.80% of Python3 online submissions for Jump Game II.
    
    def jump(self, nums) -> int:
        
        res =0
        l , r = 0, 0
        
        while r < len(nums)-1:
            farthest = 0
            for i in range (l, r+1):
                farthest = max(farthest, i+nums[i])
            l= r+1
            r = farthest
            res+=1
            
        return res
    
print(Solution().jump([1,1,1,1]))
print(Solution().jump([2,3,1,1,4]))
print(Solution().jump([2,3,0,1,4]))