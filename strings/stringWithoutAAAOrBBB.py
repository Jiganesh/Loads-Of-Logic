# https://leetcode.com/problems/string-without-aaa-or-bbb/

# Solution
# https://leetcode.com/problems/string-without-aaa-or-bbb/discuss/508543/APPLES-and-BANANAS-solution-(with-picture)

class Solution:
    
    # Naive Backtracking Solution
    
    # TC : O(2^(A*B))
    # SC : O(N)
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        self.ans = ""
        def helper(a , b, result):
            
            word="".join(result) 
            
            if self.ans != "":
                return self.ans
            
            if "aaa" in word or "bbb" in word :
                return 
            
            if a==0 and b==0:
                self.ans = word
                return 
            
            if a>0 :
                result.append("a")
                helper(a-1, b, result)
                result.pop()
            if b>0:
                result.append("b")
                helper(a, b-1, result)
                result.pop()
                
            return self.ans
        
        return helper(a, b , [])
    
    
    
    # If you do not understand this solution please check the solution reference link provided above
    
    
    # Runtime: 34 ms, faster than 86.44% of Python3 online submissions for String Without AAA or BBB.
    # Memory Usage: 13.9 MB, less than 23.00% of Python3 online submissions for String Without AAA or BBB.
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        
        laydown_character , laydown_count = max([("a", a), ("b", b)], key = lambda x : (x[1], x[0]))
        topup_character , topup_count = min([("a", a), ("b", b)], key = lambda x :  (x[1], x[0]))
        
        # As the consequtive count of a character should not increase 3
        stack = [laydown_character * 2] * (laydown_count//2) 
        if laydown_count&1:
            stack.extend([laydown_character* (laydown_count&1)])
        
        index = 0
        while topup_count >0:
            stack[index%len(stack)]+=topup_character
            topup_count-=1
            index+=1
            
        return "".join(stack)
        
            
        
        