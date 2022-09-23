# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/submissions/
class Solution:
    
    # Brute Force
    
    def numberOfSteps(self, num: int) -> int:
        
        def helper(num):
            if num<=0:
                return 0
            if num%2==0:
                return 1+ helper(num//2)
            else:
                return 1+ helper((num-1))
        return helper(num)
    
    
    # For the binary representation from right to left(until we find the leftmost 1):
    # if we meet 0, result += 1 because we are doing divide;
    # if we meet 1, result += 2 because we first do "-1" then do a divide;
    # ony exception is the leftmost 1, we just do a "-1" and it becomse 0 already.
    
    # Bit Manipulation Solution
    # Optimal
    
    def numberOfSteps(self, n: int) -> int:
        res = 0
        while n>1:
            res += (n&1)+1
            n=n>>1

                
        return res+n #because at last step when we have one left we can just take one step and reach zero
    