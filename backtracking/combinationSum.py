# https://leetcode.com/problems/combination-sum/

class Solution:
    # Runtime: 89 ms, faster than 74.78% of Python3 online submissions for Combination Sum.
    # Memory Usage: 14.3 MB, less than 9.56% of Python3 online submissions for Combination Sum.
    def combinationSum(self, candidates, target: int) :
        
        def helper (index=0, current=0 , array=[], result=[]):
            
            if current ==target:
                result.append(array[:])
                
            if current <target:
                
                for j in range (index, len(candidates)):
                    i = candidates[j]
                    if current+i<=target:
                        array.append(i)
                        helper(j, current+i, array, result)
                        array.pop()
            return result
        
        return helper()
        