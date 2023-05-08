# https://leetcode.com/problems/find-the-distinct-difference-array/description/
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        
        prefix = defaultdict(int)
        suffix = Counter(nums)
        result = []

        for num in nums:
            prefix[num]+=1
            suffix[num]-=1
            if suffix[num]==0:
                del suffix[num]

            result.append(len(prefix)- len(suffix))
        return result 

