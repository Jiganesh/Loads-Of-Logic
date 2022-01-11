# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

def getDescentPeriods(prices):
            
    #1  faster than 40% other solutions O(n)
    
    # descent=[1]*len(prices) 
    # for i in range(1, len(prices)):
    #     if prices[i-1]-prices[i]==1:
    #         descent[i]+=descent[i-1]   
    # return sum(descent)
        
    #2  Improved above solution space complexity -->O(1)
    # final, temp=1,1
    # for i in range(1, len(prices)):
    #     if prices[i-1]-prices[i]==1:
    #         temp+=1
    #     else:
    #         temp=1
    #     final+=temp
    # return final
    
    #3  Faster than 80%
    # final, temp, prev=0,1,
    # for i in prices:
    #     if prev-i==1:
    #         temp+=1
    #     else:
    #         temp=1
    #     final+=temp
    #     prev=i
    # return final

    #4  Faster than 80% other solutions (CALCULATING FORMULA)
    counter=len(prices)
    leng=1
    for i in range(1,len(prices)):
        if prices[i-1]-prices[i]==1:
            leng+=1

        else:
            counter+=(((leng-1)*leng)//2)
            leng=1
    if leng>1:
        counter+=(((leng-1)*leng)//2 )
    return counter

prices = [3,2,1,4]
print(getDescentPeriods(prices))

# Jiganesh
class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        start = 0
        end=val=1
        
        while end < len(prices):
            if (prices[end-1]-prices[end])==1:
                val+=end-start
            else :
                start=end
            val+=1
            end+=1
                
        return val