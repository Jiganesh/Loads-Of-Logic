#https://leetcode.com/problems/largest-rectangle-in-histogram/

# Solution : https://www.youtube.com/watch?v=vcv3REtIvEo (Noob Solution)
# Solution : https://www.youtube.com/watch?v=zx5Sw9130L0 (Pro Solution)

from typing import List

class Solution:
    
    # Submitted By Jiganesh
    
    # TC : O(N)
    # SC : O(N)
    
    # Strivers Solution
    
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        
        # Next Smeller Element on left Side
        
        next_smaller_element_left_side  = [0]*n
        stack = []
        
        for height_ind in range(n):
            
            while stack and heights[stack[-1]] >= heights[height_ind]:
                stack.pop()
            
            next_smaller_element_left_side[height_ind] = stack[-1]+1 if stack else 0
            stack.append(height_ind)
            
            
        # Next Smaller Element on right Side
        
        next_smaller_element_right_side = [n]*n
        stack = []
        
        for height_ind in range (n-1, -1,-1):
            
            while stack and heights[stack[-1]] >= heights[height_ind]:
                stack.pop()
            
            next_smaller_element_right_side[height_ind] = stack[-1] if stack else n
            stack.append(height_ind)
            
        
        # Find distance and calculate area
        
        max_area = 0
        
        for ind in range(n):
            
            left_index_it_can_expand = next_smaller_element_left_side[ind]
            right_index_it_can_expand = next_smaller_element_right_side[ind]
            
            area = (right_index_it_can_expand - left_index_it_can_expand)  * heights[ind]
            max_area = max(max_area, area)
        
        return max_area
    
    # Submitted by Jiganesh
    
    # TC : O(N)
    # SC : O(N)
    
    # Solution from NEETCODE
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        stack = []
        
        max_area = 0
        
        for curr_index, curr_height in enumerate(heights):
            index = curr_index
            while stack and stack[-1][1] > curr_height:

                index, height = stack.pop()
                area = (curr_index - index) * height
                max_area = max(area, max_area)
            
            stack.append([index, curr_height])
            
        for curr_index, curr_height in stack:
            area = (n-curr_index) * curr_height
            max_area = max(area, max_area)
        
        return max_area

