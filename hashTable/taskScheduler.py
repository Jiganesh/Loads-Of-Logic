# https://leetcode.com/problems/task-scheduler/

from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        char_count = [0]*26

        for task in tasks:
            index = ord(task)-65
            char_count[index]+=1

        
        char_count.sort()
        max_frequency = char_count[-1]-1
        max_slots = (max_frequency) * n

        idle_slots = max_slots

        for ind in range (24, -1, -1):
            idle_slots -= min(char_count[ind], max_frequency)

        return idle_slots > 0 and idle_slots + len(tasks) or len(tasks)
        
        