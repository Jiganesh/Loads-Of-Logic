# https://leetcode.com/problems/mice-and-cheese/

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        
        n = len(reward1) # length of reward1 and reward2 is same
        diff = []
        for ind in range(n):
            diff.append((reward2[ind]-reward1[ind], ind))

        result = 0
        diff.sort()

        for ind in range (k):
            result += reward1[diff[ind][1]]
        for ind in range (k, n):
            result += reward2[diff[ind][1]]


        return result 
     