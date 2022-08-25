# https://leetcode.com/problems/word-search/

from typing import List
from collections import Counter

class Solution:
    
    # 9763 ms
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        
        def isValid (i, j):
            return  0<=i<R and 0<=j<C
        
        def helper(i, j , board, word, pointer, visited):
            if pointer >= len(word):
                return True
            
            if isValid(i, j) and (i, j) not in visited and pointer < len(word) and board[i][j]==word[pointer] :
                
                visited.add((i,j))

                up = helper(i-1, j, board, word, pointer+1, visited)
                down = helper(i+1, j, board, word, pointer+1, visited)
                left = helper(i, j-1,board, word, pointer+1, visited )
                right = helper(i, j+1,board, word, pointer+1, visited)

                visited.remove((i,j))
                
                return up or down or left or right
            return False
 
        ans = False
        for i in range (len(board)):
            for j in range (len(board[0])):
                if board[i][j] == word[0]:
                    ans = ans or helper(i, j, board, word, 0 , set())
                if ans: return True
        return False
    
    # Optimization
     
    # Instead of add and remove operations in set use board
    
    # Runtime: 8868 ms, faster than 23.87% of Python3 online submissions for Word Search.
    #  Memory Usage: 13.9 MB, less than 92.88% of Python3 online submissions for Word Search.       
    def exist(self, board: List[List[str]], word: str) -> bool:

        R = len(board)
        C = len(board[0])
        
        def isValid (i, j):
            return  0<=i<R and 0<=j<C
        
        def helper(i, j , board, word, pointer):
            if pointer >= len(word):
                return True
            
            if isValid(i, j) and pointer < len(word) and board[i][j]==word[pointer] :
                
                temp = board[i][j]
                board[i][j] = "*"
                
                up = helper(i-1, j, board, word, pointer+1)
                down = helper(i+1, j, board, word, pointer+1)
                left = helper(i, j-1,board, word, pointer+1)
                right = helper(i, j+1,board, word, pointer+1)

                board[i][j] = temp
                
                return up or down or left or right
            return False
 
        for i in range (R):
            for j in range (C):
                if board[i][j] == word[0] and helper(i, j, board, word, 0):
                    return True
        return False
    
    # Search and Prune Technique Optimization
        
    # Runtime: 41 ms, faster than 99.83% of Python3 online submissions for Word Search.
    # Memory Usage: 13.9 MB, less than 92.88% of Python3 online submissions for Word Search.
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        
        word_dictionary = Counter(word)
        board_dictionary = Counter()
        
        for row in board:
            board_dictionary += Counter(row)

        # Edge Case 1 (helps in optimization)
        # If characters in word are more than that character in board:
        # The word can never be made
        
        for w, c in word_dictionary.items():
            if board_dictionary[w] < c:
                return False
        
        # Case 2 (helps in optimization):
        if word_dictionary[word[0]] > word_dictionary[word[-1]]:
            word = word[::-1]
        
        
        def isValid (i, j):
            return  0<=i<R and 0<=j<C
        
        def helper(i, j , board, word, pointer):
            if pointer >= len(word):
                return True
            
            if isValid(i, j) and pointer < len(word) and board[i][j]==word[pointer] :
                
                temp = board[i][j]
                board[i][j] = "*"
                
                up = helper(i-1, j, board, word, pointer+1)
                down = helper(i+1, j, board, word, pointer+1)
                left = helper(i, j-1,board, word, pointer+1)
                right = helper(i, j+1,board, word, pointer+1)

                board[i][j] = temp
                
                return up or down or left or right
            return False

        for i in range (R):
            for j in range (C):
                if board[i][j] == word[0] and helper(i, j, board, word, 0):
                    return True
        return False
        
                