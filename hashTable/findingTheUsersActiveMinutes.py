# https://leetcode.com/problems/finding-the-users-active-minutes/

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:


        time_freq = defaultdict(set)

        for id, time in logs:
            time_freq[id].add(time)

        result = [0] * k
        for id, times in time_freq.items():
            UAM = len(times)
            result[UAM-1]+=1

        return result
