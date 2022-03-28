# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution:

    # TC : O(N)
    # SC : O(N)

    # Runtime: 27 ms, faster than 42.61% of Python online submissions for Letter Combinations of a Phone Number.
    # Memory Usage: 13.5 MB, less than 66.02% of Python online submissions for Letter Combinations of a Phone Number.

    def letterCombinations(self, digits):

        if len(digits) <= 0:
            return []

        dictionary = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def dfs(dictionary, index, array, result):

            if index == len(digits):
                result.append("".join(array[:]))
                return

            for i in dictionary[digits[index]]:
                array.append(i)
                dfs(dictionary, index+1, array, result)
                array.pop()

            return result
        index = 0
        array = []
        result = []
        return dfs(dictionary, index, array, result)

    # Runtime: 16 ms, faster than 89.69% of Python online submissions for Letter Combinations of a Phone Number.
    # Memory Usage: 13.5 MB, less than 38.81% of Python online submissions for Letter Combinations of a Phone Number.

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        dictionary = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def helper(dictionary, array=[], result=[], index=0):

            if index > len(digits)-1:
                result.append("".join(array[:]))

            if index <= len(digits)-1:
                listofdigit = dictionary[digits[index]]
                for i in listofdigit:

                    array.append(i)
                    helper(dictionary, array, result, index+1)
                    array.pop()

            return result

        array, result, index = [], [], 0
        res = helper(dictionary, array, result, index)
        return res


# ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(Solution().letterCombinations("23"))
print(Solution().letterCombinations(""))  # []
print(Solution().letterCombinations("2"))  # ["a","b","c"]
