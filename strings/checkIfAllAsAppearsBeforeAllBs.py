# Problem Link: https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/submissions/

class Solution:
    def checkString(self, s: str) -> bool:
        last_seen = 'a'
        for i in s:
            if last_seen == 'a' and i == 'b':
                last_seen = 'b'
            elif last_seen == 'b' and i == 'a':
                return False
        return True
#         In this problem, we set the last seen element, initially as 'a'
#         If the next element we see is 'a', we move ahead,
#         else if the next element we see in 'b', we set the last seem to be 'b'
#         If my last seen in 'b' and I encounter 'a', I return False
       