# https://leetcode.com/problems/combination-sum/


class Solution(object):
    
    # Submitted by Jiganesh
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.helper(candidates, target,[],0, [] )
        
    
    def helper(self, candidates, target, array,start=0 ,result=[]):
        
        if target ==0:
            result.append(array[:])
            return
        
        if target>0:
            
            for i in range(start,len(candidates)):
                num  = candidates[i]
                array.append(num)
                self.helper(candidates, target-num, array,i, result)
                array.pop()
                
        return result
        