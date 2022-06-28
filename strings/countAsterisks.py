# https://leetcode.com/problems/count-asterisks/

class Solution:

    # Runtime: 56 ms, faster than 39.97% of Python3 online submissions for Count Asterisks.
    # Memory Usage: 13.8 MB, less than 97.89% of Python3 online submissions for Count Asterisks.


    # TC : O(N)
    # SC : O(N)
    def countAsterisks(self, s: str) -> int:

        blocks = s.split("|")

        result = 0

        for i in range (len(blocks)):
            if i%2==0 : result += blocks[i].count("*")

        return result

    # One liner

    # TC : O(N)
    # SC : O(N)
    def countAsterisks(self, s: str) -> int:

        return sum([i.count("*") for i in s.split("|")[0::2]])

    # Optimal Solution
    # TC : O(N)
    # SC : O(1)

    # Runtime: 35 ms, faster than 91.95% of Python3 online submissions for Count Asterisks.
    # Memory Usage: 13.8 MB, less than 97.89% of Python3 online submissions for Count Asterisks.
    
    def countAsterisks(self, s: str) -> int:

        bars = 0
        result = 0

        for i in s :
            if i=="*" and bars%2==0:
                result+=1
            elif i=="|":
                bars+=1
        return result