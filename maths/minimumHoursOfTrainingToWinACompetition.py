# https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/

from typing import List
class Solution:
    
    # Runtime: 47 ms, faster than 100.00% of Python3 online submissions for Minimum Hours of Training to Win a Competition.
    # Memory Usage: 14 MB, less than 33.33% of Python3 online submissions for Minimum Hours of Training to Win a Competition.
    
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        
        max_needed_days_energy = max(sum(energy)-initialEnergy+1, 0)
        
        max_needed_days_experience = 0
        
        for e in experience:
            if e >= initialExperience:
                neededExperience = (e - initialExperience + 1)
                max_needed_days_experience = max(neededExperience, max_needed_days_experience)
            initialExperience+=e
        
        return max_needed_days_experience + max_needed_days_energy
