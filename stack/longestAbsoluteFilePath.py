# https://leetcode.com/problems/longest-absolute-file-path/

class Solution:

    def lengthLongestPath(self, string: str) -> int:
        array = string.split("\n")

        stack = []

        result = 0

        for i in array:
            count_t = i.count("\t")
            while  stack and count_t <= stack[-1].count("\t"):
                stack.pop()
            else:

                stack.append(i)
                # print(stack)

                if "." in i:

                    r = [i.replace("\t", "") for i in stack]
                    ans = len("".join(r))+ len(r)-1
                    result = max(result, ans)

        return result

    # Runtime: 24 ms, faster than 99.16% of Python3 online submissions for Longest Absolute File Path.
    # Memory Usage: 13.9 MB, less than 76.69% of Python3 online submissions for Longest Absolute File Path.

    def lengthLongestPath(self, string: str) -> int:
        array = string.split("\n")

        def word_to_level_length(word):

            n = len(word.replace("\t", ""))
            level = word.count("\t")
            is_file = "." in word
            return (level, n, is_file)

        lookup = [word_to_level_length(word) for word in array]

        result = 0
        stack = [(float("-inf"), 0)]

        for level, length, is_file in lookup:

            while stack and stack[-1][0] >= level:
                stack.pop()
            else:
                stack.append((level, stack[-1][1]+length, is_file))

                if is_file:
                    result = max(result,  stack[-1][1]+level)  # ultimately level is number of / in between

        return result