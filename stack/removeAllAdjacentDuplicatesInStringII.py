# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
class Solution:
    
    # Runtime: 210 ms, faster than 27.03% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
    # Memory Usage: 18.7 MB, less than 69.77% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
    
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        for i in s :
            if not stack or stack[-1][0]!=i:
                stack.append([i, 1])
            else:
                val = stack.pop()
                val[1]+=1
                stack.append(val)
                if stack[-1][1]==k:
                    stack.pop()
                    
        
        return "".join([i[0]*i[1] for i in stack])
        