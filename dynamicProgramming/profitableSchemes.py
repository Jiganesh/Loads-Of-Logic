# https://leetcode.com/problems/profitable-schemes/

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:

        MOD = 10 ** 9 + 7
        G = len(group)

        has_cache = [[[False]* (minProfit+1) for _ in range(G)] for _ in range(n+1)]
        cache = [[[None]* (minProfit+1) for _ in range(G)] for _ in range(n+1)]

        def helper(people_left, index, profit_left):

            

            if people_left  < 0:
                return 0

            if profit_left <= 0:
                profit_left = 0
            
            if index >= G :
                if profit_left <= 0:
                    return 1
                return 0 
                
            if has_cache[people_left][index][profit_left]:
                return cache[people_left][index][profit_left]

            taking_scheme = helper(people_left - group[index], index+1, profit_left - profit[index])
            not_taking_scheme = helper(people_left, index+1, profit_left)

            cache[people_left][index][profit_left] = (taking_scheme + not_taking_scheme) % MOD
            has_cache[people_left][index][profit_left] = True
            return  cache[people_left][index][profit_left]

        return helper(n, 0, minProfit)