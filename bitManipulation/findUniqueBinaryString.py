# https://leetcode.com/problems/find-unique-binary-string/


class Solution:

    # Cantor's diagonal Argument - Only possible when unique and n * n arguments
    # TC : O(N)
    # SC : O(N)
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        new_num = ""
        for ind, num in enumerate(nums):
            new_num  +=  num[ind]=="1" and "0" or "1"
        return new_num
       