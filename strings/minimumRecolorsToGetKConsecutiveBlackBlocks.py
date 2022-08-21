# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
class Solution:
    
    # Runtime: 34 ms, faster than 80.00% of Python3 online submissions for Minimum Recolors to Get K Consecutive Black Blocks.
    # Memory Usage: 13.9 MB, less than 20.00% of Python3 online submissions for Minimum Recolors to Get K Consecutive Black Blocks.
    
    # TC : O(N)
    # SC : O(1)
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        
        pointer = 0
        current = 0
        
        while pointer < k:
            current+= blocks[pointer]=="W"
            pointer+=1

        result = current
        
        while pointer < len(blocks):
            if blocks[pointer]=="W":
                current +=1
            if blocks[pointer-k]=="W":
                current-=1
            pointer+=1
            
            result = min(current, result)
        return result
    
    # Aesthetic Solution
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        count_of_black = 0
        maximum_black_in_window = 0
        
        for ind , ch in enumerate(blocks):
            count_of_black += ch == "B"
            if ind>=k and blocks[ind-k] == "B":
                count_of_black -=1
            maximum_black_in_window = max(maximum_black_in_window, count_of_black)
            
        return k - maximum_black_in_window
    
    # One Liner Solution
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        array = [blocks[i: i+k].count("W") for i in range  (len(blocks)-k+1)]
        return min(array)
    
    