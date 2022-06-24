# https://leetcode.com/problems/construct-target-array-with-multiple-sums/

import heapq
from typing import List

# Conditions : https://www.youtube.com/watch?v=h9t7JF50Mpw



class Solution:
    
    # Runtime: 540 ms, faster than 18.82% of Python3 online submissions for Construct Target Array With Multiple Sums.
    # Memory Usage: 20 MB, less than 55.29% of Python3 online submissions for Construct Target Array With Multiple Sums.
    def isPossible(self, target: List[int]) -> bool:
        
        total_sum = sum(target)
        
        heap  = [-i for i in target]
        heapq.heapify(heap)
        
        while heap[0] != -1:
            
            max_in_heap = - heapq.heappop(heap)
            sum_of_remaining_elements = total_sum - max_in_heap

            # old logic
            # replace_value = max_in_heap - sum_of_remaining_elements

            
            # some condition we need to look out for 
            # condition 1
            # heap : 1 2 2  max = 2 total = 5 and sum of remaining elements = 3 and replace 2 will be 2 - 3 hence -1 which is false  
            # hence when sum_of_remaining_values < replace we should return false
        
            # condition 2
            # heap = 2  max = 2 and sum of remaining elements = 0 and replace 2 will be 2 -0 =2 we will be caught into infinite loop:
            # hence when sum_of_remaining_value = 0 return false
            
            # condition 3
            # heap 1 9 max 9 total = 10 and sum of remaining elements = 1  replace 9 will be 9 - 1 = 8 and it will be going on........
            # 8- 1 =7 and 7-1=6 ........... 2-1 = 1 eventually we will return true
            
            #condition 4
            # But at this point, we'll still obtain a TLE result and will need to optimize some more. Consider the situation in which we process the max value only to find that we're about to reinsert a number that is still the max value. In some edge cases, it could take thousands of iterations to fully process this value so that we can move on to another, when all that processing can be done more simply in one step.

            #Take, for example, target = [3,5,33]. Normally, we'd remove the 33 and compute its replacement to be 25, then from 25 to 17, then 17 to 9, then finally 9 to 1. Each time, we're removing the sum of all the remaining values (3 + 5 = 8) from the current number. In any valid target array, as we noted at the very beginning, the max value must be larger than the sum of the remaining elements, since it came from that sum plus the value that was replaced.

            #That means that we should be able to remove the remaining sum (8) from our current max value (33) as many times as we possibly can, since only the remainder will bring us below that sum. This we can achieve quite easily with the mod operator which will result in our replacement value (33 % 8 = 1) without the need to iterate through every step.
            
            # Ater using % operator in logic we get one more edge case
            # condition 5 
            # heap = 20 , 5 max = 20 , remaining sum = 5  if max % sum_of_remaining  == 0 hence replace will be 0 return false as we want 1 in target array
            
            
            if max_in_heap == 1 or sum_of_remaining_elements==1: return True
            if max_in_heap < sum_of_remaining_elements or sum_of_remaining_elements==0  or max_in_heap % sum_of_remaining_elements == 0 : return False
            
            max_in_heap %= sum_of_remaining_elements
            total_sum = sum_of_remaining_elements+ max_in_heap
            
            heapq.heappush(heap,-max_in_heap)

        return True
        
            
            
            
            
            