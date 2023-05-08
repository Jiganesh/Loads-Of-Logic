# https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        
        
        elements = [0] * n # This will simulate the problem
        
        result = 0  # keeps record of current adjacent element with same color
        
        array = [] # This array will be our output
        
        # check function takes 
            # number of current adjacent element with same color
            # earlier color on index we about to change
            # index to check = comp_index
            # index which will have color change
            # color on new index
            
        def check(result, earlier_color, comp_index, index, color): 
            
            # if the comp_index is in bounds
            if 0 <= comp_index < n :
                
                # check if colored and comp_index has same earlier_color if yes that means the number of adjacent element with same color will be reduced by 1
                if earlier_color and elements[comp_index] == earlier_color:
                    result-=1
                # check if colored and comp_index has same color if yes that means the number of adjacent elements with same color will increase by 1
                if color and color == elements[comp_index]:
                    result +=1
                    
            return result
            
        
        for index, color in queries:
            earlier_color = elements[index]
            # check for previous element
            result = check(result, earlier_color, index - 1, index, color)
            # check for next element
            result = check(result, earlier_color, index + 1, index, color)
            
            elements[index] = color
            
            array.append(result)
            
        return array
        