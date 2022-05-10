# https://leetcode.com/problems/combination-sum-iii/
class Solution:
    
    # Runtime: 33 ms, faster than 84.45% of Python3 online submissions for Combination Sum III.
    # Memory Usage: 13.9 MB, less than 29.87% of Python3 online submissions for Combination Sum III.
    
    def combinationSum3(self, k: int, n: int)  :
        
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        def helper(k, n, index, array, result):
            
            if len(array)==k and n ==0:
                result.append(array[:])
                
            else:
                
                for i in range (index, len(numbers)):
                    if numbers[i]<=n:
                        array.append(numbers[i])
                        helper(k , n-numbers[i], i+1, array, result)
                        array.pop()
                        
            return result
        
        array =[]
        result = []
        ans = helper(k, n, 0,array, result)
        return ans
                        
                
        
        
        