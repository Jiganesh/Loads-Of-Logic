# https://leetcode.com/problems/insert-interval/

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.append(newInterval)
        intervals.sort()
        print(intervals)

        result = []

        prev = intervals[0]

        for i in range (1, len(intervals)):
            start, end = intervals[i]

            if prev[0]<= start <= prev[1]:
                prev[1]= max(prev[1], end)
            else:
                result.append(prev)
                prev=[start, end]

        result.append(prev)
        return result
