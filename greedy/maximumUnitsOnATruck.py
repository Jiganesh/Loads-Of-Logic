# https://leetcode.com/problems/maximum-units-on-a-truck/

from typing import List
import heapq

class Solution:
    
    # Runtime: 205 ms, faster than 67.59% of Python3 online submissions for Maximum Units on a Truck.
    # Memory Usage: 14.5 MB, less than 5.52% of Python3 online submissions for Maximum Units on a Truck.
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        
        heap = []
        for number_of_boxes, number_of_units_per_box in boxTypes:
            heapq.heappush(heap, (-number_of_units_per_box, number_of_boxes))
            
        
        maximum_total_units = 0
        print(sorted(heap))
        
        while heap and truckSize >0:
            number_of_units_per_box, number_of_boxes = heapq.heappop(heap)
            boxes_taken = min (truckSize, number_of_boxes)
            maximum_total_units += boxes_taken * -number_of_units_per_box
            
            truckSize-= boxes_taken
            
        return maximum_total_units
    
    # Little Bit Optimized
    
    
    # Runtime: 172 ms, faster than 84.82% of Python3 online submissions for Maximum Units on a Truck.
    # Memory Usage: 14.4 MB, less than 32.64% of Python3 online submissions for Maximum Units on a Truck.
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        
        boxTypes.sort(key = lambda x : (-x[1], x[0]))
        
        maximum = 0
        index = 0
        while index < len(boxTypes) and truckSize:
            boxes_taken = min(truckSize, boxTypes[index][0])
            maximum += boxes_taken*boxTypes[index][1]
            
            index+=1
            truckSize-=boxes_taken
            
        return maximum