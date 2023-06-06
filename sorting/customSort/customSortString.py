# https://leetcode.com/problems/custom-sort-string/

class Solution:
    def customSortString(self, order: str, s: str) -> str:

        lookup = {i : ind for ind , i in enumerate(order)}
        s = sorted(s , key= lambda x: lookup[x] if x in lookup else -1)
        return "".join(s)