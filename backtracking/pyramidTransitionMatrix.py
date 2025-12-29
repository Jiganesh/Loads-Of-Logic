# https://leetcode.com/problems/pyramid-transition-matrix/

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:

        mapper = defaultdict(set)
        for word in allowed:
            mapper[word[:2]].add(word[-1])

        memoization = defaultdict(bool)
        

        def solve (ind, curr, above):
            
        
            if memoization[(ind,curr,above)] :
                return memoization[(ind,curr,above)]
            
            if len(curr) == 1 : 
                return True

            if ind == len(curr)-1:
                return solve(0, above, "")

            ans = False
            prefix = curr[ind:ind+2]
            if mapper[prefix]:
                for word in mapper[prefix] : 
                    ans = solve (ind+1, curr, above+word)
                    if ans : 
                        memoization[(ind,curr,above)] = True
                        return True
                    
            memoization[(ind,curr,above)] = False        
            return ans
        
        return solve(0, bottom, "")