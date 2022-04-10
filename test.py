class Solution:
    def largestInteger(self, num: int) -> int:
        
        s = list(str(num)) # Converting num to list for easy manipulations
        
        # Loops through all numbers and just check the given condition
        for i in range (len(s)):
            for j in range (i+1,len(s)):
                
                # makes sense to swap when the number ahead is smaller than number behind cause we want greater number
                # AND operator helps to check parity
                
                if int(s[i]) < int(s[j]) and int(s[i])&1==int(s[j])&1:
    
                    s[i],s[j] =s[j],s[i]
                    
        # returning Number
        return "".join(s)
    
    







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
    
    
import heapq
class Solution:
    def maximumProduct(self, nums, k: int) -> int:
        
        # creating a heap
        heap = []
        for i in nums:
            heapq.heappush (heap,i)
            
            
        # basic idea here is keep on incrementing smallest number then only multiplication of that number will be greater
        # so basically till I have operations left I will increment my smallest number
        while k :
            current = heapq.heappop(heap)
            heapq.heappush(heap, current+1)
            k-=1
            
        result =1
        
        # Just Multiply all the numbers in heap and return the value
        while len(heap)>0:
            x= heapq.heappop(heap)
            result =(result*x )% (10**9+7)
            
        return result