# https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        
        MOD = 10**9 + 7
        
        ranges.sort(key = lambda x : (x[0], x[1]))
        n = len(ranges)        
        # result = []
        
        pack = 1
        start , end = ranges[0]
        for i in range ( 1, n ) :
            s, e = ranges[i]
            if start<= s <= end :
                end = max(e, end)
                start = min(s, start)
            else:
                # result.append([start, end])
                start = s
                end = e
                
                pack +=1
                
        # result.append([start, end])
        # print(result)

        return 2 ** pack % MOD