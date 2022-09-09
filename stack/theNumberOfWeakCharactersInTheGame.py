class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        stack = []
        count = 0
        
        properties.sort(key = lambda x : (x[0], -x[1]))
        
        for character in properties:
            attack, defence = character
            while stack and stack[-1][0]< attack and stack[-1][1]< defence:
                count+=1
                stack.pop()
            stack.append([attack, defence])
                
        return count
    
"""
Input :
[[1,1],[2,1],[2,2],[1,2]]
"""