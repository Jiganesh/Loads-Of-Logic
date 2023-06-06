# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

from typing import List

class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:

        n = len(words)
        result = float("inf")
        for ind, word in enumerate(words):
            if word == target:
                distance_front = ind - startIndex
                distance_behind = n - abs(ind-startIndex)
                
                minimum_dist = min(abs(distance_front), abs(distance_behind))
                result = min(result, minimum_dist)

        return result if result != float("inf") else -1
