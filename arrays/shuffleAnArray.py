# https://leetcode.com/problems/shuffle-an-array/

class Solution:

    def __init__(self, nums: List[int]):
        self.length = len(nums)
        self.nums = nums
        self.nums_copy = nums[:]
        

    def reset(self) -> List[int]:
        self.nums = self.nums_copy[:]
        return self.nums
        
    def swap (self, ind1, ind2):
        self.nums[ind1], self.nums[ind2] = self.nums[ind2], self.nums[ind1]

    def shuffle(self) -> List[int]:

        for ind in range (self.length):
            random_index = randint(ind, self.length-1)
            self.swap(ind, random_index)
        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()