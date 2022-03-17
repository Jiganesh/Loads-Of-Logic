# https://leetcode.com/problems/sort-the-jumbled-numbers/
class Solution(object):
    
    # Runtime: 1448 ms, faster than 97.78% of Python online submissions for Sort the Jumbled Numbers.
    # Memory Usage: 19.9 MB, less than 87.41% of Python online submissions for Sort the Jumbled Numbers.
    
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """

        def valueFromMapping(number):

            if number == 0:
                return mapping[0]

            newNum = 0
            mul = 0

            while number:
                newNum = mapping[number % 10]*(10**mul) + newNum
                number = number//10
                mul += 1

            return newNum

        return sorted(nums, key=valueFromMapping)
