class Solution(object):
    
    # TC : O(N)
    # SC : O(N)
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        # Example :
        # If we have 8759 as a four digit number
        
        # To make a smaller sum we will obviously need smaller numbers
        # Hence to make the smaller numbers break them into individual digits and sort the numbers
        
        # after sorting we have [5, 7, 8, 9]
        # then we pick a least possible for tens position and max possible for ones position
        # like 5 and 7 for tens position and 9 and 8 for unit digits position        # you can also pick 5 and 8 and 7 and 9 it doesnt matter as long as your tens digits are least from array
        
        # 59 + 78 = 137
        # This will be the answer
        
        # Another Example : 4009
        # after sorting [0, 0, 4, 9]
        # after picking 09 + 04 OR 04 + 09  both equals 13
        
        # Another Example : 2932
        # after sorting [2, 2, 3, 9]
        # after picking 29 +23 OR 23 +29 both equals 52
        
        # Another Example : 2675
        # after sorting [2, 5, 6, 7]
        # after picking 27 + 56 OR 57+26  both equals 83
        
        

        # Method 1 :
        
        a = sorted([i for i in str(num)])
        num1 = a[0]+a[3]
        num2 = a[1]+a[2]
                
        return int(num1)+int(num2)  
    
        # Method 2 :
        arr=[]
        
        while num:
            arr.append(num%10)
            num//=10
        return (arr[0]*10+arr[3]) + (arr[1]*10+arr[2])
            
        