# https://leetcode.com/problems/unique-length-3-palindromic-subsequences

class Solution:

    # TC : O(26 * N)
    # SC : O(N)

    def countPalindromicSubsequence(self, s: str) -> int:

        indexes_dict = defaultdict(list)
        result = 0

        for ind, ch in enumerate(s):
            indexes_dict[ch].append(ind)

        for key, value in indexes_dict.items():
            start, end  = value[0], value[-1]

            unique_ch = set(s[start+1:end])
            result += len(unique_ch)

        return result