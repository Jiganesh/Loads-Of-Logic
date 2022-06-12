# https://leetcode.com/problems/minimum-operations-to-convert-number/

from collections import deque

class Solution:
    
    # Runtime: 2289 ms, faster than 71.00% of Python3 online submissions for Minimum Operations to Convert Number.
    # Memory Usage: 14 MB, less than 97.00% of Python3 online submissions for Minimum Operations to Convert Number.
    
    def minimumOperations(self, nums, start: int, goal: int) -> int:
        
        def breadth_first_search (nums, start, goal):
            
            queue = deque()
            queue.append((start, 0)) #current Number and operations done 
            lookup = set()
            
            while queue:
                val, operations = queue.popleft()
                
                for i in nums:
                    for operation_on_val in (val+i, val-i, val^i):
                        
                        if operation_on_val == goal:
                            return operations+1
                        
                        if 0<=operation_on_val<=1000 and operation_on_val not in lookup:
                            
                            lookup.add(operation_on_val)
                            queue.append((operation_on_val,operations+1))
                            
            return -1
                            
        return breadth_first_search(nums, start, goal)