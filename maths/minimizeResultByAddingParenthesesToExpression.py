class Solution:
    def minimizeResult(self, expression: str) -> str:
        
        # to store minimum answer
        minans = float('inf')
        
        # result stores parenthesized string for the given expression
        result = ""
        
        # spliting both numbers
        num1, num2 = expression.split("+")
        
        
        # traversing from behind of first number
        for i in range (len(num1)-1, -1, -1):
            
            # traversing from front of second number
            for j in range(1, len(num2)+1):
                
                
                # checking each and every combination 
                
                # as we multiply extreme rightside and leftside if those values are null assigning them to 1 cz its multiplication
                # as we add middle rightParen and leftParen if those values are null assiging them to 0 cz its addition duh !
                
                rightside = int(num1[0:i]) if num1[0:i] else 1
                rightParen = int(num1[i:]) if num1[i:] else 0
                
                leftParen = int(num2[:j]) if num2[:j] else 0
                leftside = int(num2[j:]) if num2[j:] else 1
                
                
                current = rightside* (rightParen+ leftParen) * leftside

                # if current is minimum then just update your result and don't forget to update your minimum answer as well
                if current < minans :
                    
                    result = num1[0:i] +"("+ num1[i:]+"+"+num2[:j]+")"+num2[j:]
                    minans = current
                    
        # return parenthesized string 
        return result
                            