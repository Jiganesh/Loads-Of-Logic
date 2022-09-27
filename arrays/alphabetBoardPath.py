# https://leetcode.com/problems/alphabet-board-path/

class Solution:
    
    # Runtime: 71 ms, faster than 12.71% of Python3 online submissions for Alphabet Board Path.
    # Memory Usage: 13.8 MB, less than 99.15% of Python3 online submissions for Alphabet Board Path.
    
    def alphabetBoardPath(self, target: str) -> str:
        
        board = {ch:[ind//5, ind%5] for ind , ch in enumerate("abcdefghijklmnopqrstuvwxyz")}
        
        x0, y0 = 0, 0
        
        res = []
        # Order matters L U should come first before R D
        
        for ch in target:
            x, y = board[ch]
            if y < y0: res.append('L' * (y0 - y))
            if x < x0: res.append('U' * (x0 - x))
            if x > x0: res.append('D' * (x - x0))
            if y > y0: res.append('R' * (y - y0))
            res.append("!")
            x0, y0 = x,y
            
        return "".join(res)
            