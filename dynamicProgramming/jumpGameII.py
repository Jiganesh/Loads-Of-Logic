# https://leetcode.com/problems/jump-game-ii/

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
    
    def jump(self, nums) -> int:

        size = len(nums)
        # destination is last index
        destination = size - 1
        
        # record of current coverage, record of last jump index
        cur_coverage, last_jump_index = 0, 0
        
        # counter for jump
        times_of_jump = 0
        
         # Quick response if start index == destination index == 0
        if size == 1:
            return 0
        
        
        # Greedy strategy: extend coverage as long as possible with lazy jump
        for i in range( 0, size):
            
            # extend current coverage as further as possible
            cur_coverage = max( cur_coverage, i + nums[i] )
            

            # forced to jump (by lazy jump) to extend coverage  
            if i == last_jump_index:
            
                # update last jump index
                last_jump_index = cur_coverage
                
                # update counter of jump by +1
                times_of_jump += 1
                
                # check if reached destination already
                if cur_coverage >= destination:
                        return times_of_jump
                
        return times_of_jump
    
print(Solution().jump([1,1,1,1]))
print(Solution().jump([2,3,1,1,4]))
print(Solution().jump([2,3,0,1,4]))