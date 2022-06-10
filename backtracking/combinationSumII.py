# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    
    # Runtime: 90 ms, faster than 64.03% of Python3 online submissions for Combination Sum II.
    # Memory Usage: 14.2 MB, less than 5.29% of Python3 online submissions for Combination Sum II.
    
    def combinationSum2(self, candidates, target):
        
        def helper (index=0 , current=0 , array=[] , result=set()):
            
            if current==target:
                result.add(tuple(array[:]))
                return
            
            if current < target:
                for i in range (index, len(candidates)):
                    if i > index and candidates[i-1]==candidates[i]:     # IMP
                        continue
                    if current +candidates[i]<=target:
                        
                        array.append(candidates[i])
                        helper(i+1, current+candidates[i], array, result)
                        array.pop()
                    
            return result
        
        candidates.sort()
        if sum(candidates)< target:
            return []
        return helper()
    
'''

# Very important here! We don't use `i > 0` because we always want 
# to count the first element in this recursive step even if it is the same 
# as one before. To avoid overcounting, we just ignore the duplicates
# after the first element.
        
To folks who are uncertain about the nums[i] == nums[i - 1] skips. The algorithm in this solution is basically trying out different element to place after the current path:

nums: 1a,1b,2,5,6,7,10 (here, 1a and 1b are both 1s)
Let see what would happen if we did not skip when `nums[i] == nums[i - 1]`:

current_path                current_target                    remaining_next_candidates
[1a]                             7                                  [1b,2,5,6,7...
    [1a,1b]                         6                                   [2,5,6,7...
    [1a,2]                          5                                   [5,6,7...
    [1a,5]                          2                                   [6,7...
[1b]                             7                                  [2,5,6,7...
    [1b,2]                          5                                   [5,6,7...
    [1b,5]                          2                                   [6,7...

Notice how the [1,2] and [1,5] are repeated? because we are treating [1a] and [1b] as completely different paths, but they both led to a path where a single-2 follows immediately a single-1, as well a single-5 follows immediately a single-1

'''
                
            
        