

class Solution(object):
    
    
    # Finding Three Consequtive Numbers which sum to given number

    # Lets Understand the equation

    # Consider the Number x then the consequtive Number to x will be x+1 and x+2

    # Hence the sum of consequtive three Numbers will be equal to Num
    # (x)+(x+1)+(x+2) = num
    # 3*x +3 = num
    # x= (num-3)//3

    # if sum of (x, x+1, x+2) == num then return them as array [x, x+1, x+2]
    # else return empty array


    # Submitted By @Jiganesh
    # TC : O(1)
    # SC : O(N)

    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        d = (num - 3)/3 
        return  [d, d+1,d+2] if 3*d+3 == num else []
    
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        return [(num//3)-1, num//3,(num//3)+1] if num%3 == 0 else []
    
print(Solution().sumOfThree(6))
print(Solution().sumOfThree(33))

