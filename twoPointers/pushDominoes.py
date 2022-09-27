# https://leetcode.com/problems/push-dominoes/

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        
        dominoes = list(dominoes)
        
        left_array = [float("inf")]*n
        right_array = [float("inf")]*n
        
        left_falling = 0
        left_force = False
        
        for ind in range (n-1, -1, -1):
            if dominoes[ind]=="L":
                left_falling=1
                left_force = True
            elif dominoes[ind]=="." and left_force:
                left_array[ind]=left_falling
                left_falling+=1
            else:
                left_falling=0
                left_force = False
        
        right_falling = 0
        right_force = False
        
        for ind in range(n):
            if dominoes[ind]=="R":
                right_falling=1
                right_force = True
            elif dominoes[ind]=="." and right_force:
                right_array[ind]=right_falling
                right_falling+=1
            else:
                right_falling=0
                right_force = False
                
        # print(dominoes)
        # print(left_array)
        # print(right_array)
        
        for ind in range(n):
            if dominoes[ind]==".":
                
                if right_array[ind]<left_array[ind]:
                    dominoes[ind]="R"
                elif left_array[ind]<right_array[ind]:
                    dominoes[ind]="L"
                
                
        return ''.join(dominoes)