class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        array =[0]+[3**i for i in range (0, 20) if (3**i) <= (10**7) ]

        def helper( index, target):
            if target == 0:
                return True

            if target > 0:
                ans = False
                for ind in range (index+1, len(array)):
                    ans = ans or helper(ind, target-array[ind])

                return ans
        
        return helper(0, n)
    
    