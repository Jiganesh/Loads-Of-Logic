# Fisher Yates Algorithm
# https://leetcode.com/problems/random-pick-index/


class Solution:

    def __init__(self, nums: List[int]):

        self.lookup = defaultdict(list)
        for ind, num in enumerate(nums):
            self.lookup[num].append(ind)


    def pick(self, target: int) -> int:
        arr = self.lookup[target]
        n = len(arr)
        return arr[randint(0, n-1)]
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)