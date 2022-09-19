# https://leetcode.com/problems/find-duplicate-file-in-system/

from typing import List
from collections import defaultdict

class Solution:
    
    # Runtime: 139 ms, faster than 60.00% of Python3 online submissions for Find Duplicate File in System.
    # Memory Usage: 24 MB, less than 54.58% of Python3 online submissions for Find Duplicate File in System.
    
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        def in_between (string):
            word_start_index = string.find("(")+1
            word_end_index = string.find(")")
            return string[: word_start_index-1], string[word_start_index: word_end_index]
            
        result = defaultdict(list)
        
        for root in paths:
            
            files = root.split(" ")
            directory = files.pop(0)
            
            for file in files:
                path, content = in_between(file)
                
                result[content].append(directory + "/" + path)
                
        return [value for key, value in result.items() if len(value)>1]