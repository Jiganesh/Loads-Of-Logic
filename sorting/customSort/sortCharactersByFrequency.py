# https://leetcode.com/problems/sort-characters-by-frequency/

from itertools import Counter
class Solution:
    def frequencySort(self, s: str) -> str:

        d = Counter(s)
        value_key_pair = [(value , key) for key , value in  d.items()]
        value_key_pair.sort(reverse=True)
        return "".join(value*key for value, key in value_key_pair)
