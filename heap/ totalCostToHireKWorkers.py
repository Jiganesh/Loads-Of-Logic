# https://leetcode.com/problems/total-cost-to-hire-k-workers/

from typing import List
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        leftheap = []
        rightheap = []
        
        left = 0 
        right = len(costs)-1

        answer = 0


        while k > 0 :

            while left <= right and len(leftheap) < candidates:
                heapq.heappush(leftheap, (costs[left], left))
                left+=1
            
            while right >= left and len(rightheap) < candidates:
                heapq.heappush(rightheap, (costs[right], right))
                right-=1


            leftcandidate_cost, left_ind =  leftheap[0] if leftheap else (float("inf"), float("inf"))
            rightcandidate_cost, right_ind = rightheap[0] if rightheap else (float("inf"), float("inf"))

            if (leftcandidate_cost, left_ind) < (rightcandidate_cost, right_ind):
                heapq. heappop(leftheap)
            else:
                heapq.heappop(rightheap)
            
            answer += min(leftcandidate_cost, rightcandidate_cost)
            
            k-=1

        return answer
