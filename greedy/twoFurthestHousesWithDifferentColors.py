# https://leetcode.com/problems/two-furthest-houses-with-different-colors/

from typing import List

class Solution:

    # Runtime: 53 ms, faster than 73.08% of Python3 online submissions for Two Furthest Houses With Different Colors.
    # Memory Usage: 13.7 MB, less than 96.95% of Python3 online submissions for Two Furthest Houses With Different Colors.

    # TC : O(N)
    # SC : O(1)
    
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        first_house_color = colors[0]
        last_house_color = colors[-1]

        for ind, house_color in enumerate(colors):
            if house_color != first_house_color : ans = max(ans, ind-0)
            if house_color != last_house_color : ans = max(ans, len(colors)-1-ind)

        return ans