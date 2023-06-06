# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/
# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/solutions/2754088/python-c-java-rust-intuitive-visual-concise-calculation-of-time-with-detailed-comments/


from typing import List
class Solution:
    
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:


        plant_grow = list(zip( growTime, plantTime))
        plant_grow.sort(reverse= True)


        min_time = current_time = 0
        for growth, planting in plant_grow:
            current_time += planting
            min_time = max(min_time, current_time + growth)
        
        return min_time
