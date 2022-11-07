class Solution:
    def maximum69Number (self, num: int) -> int:

        # find first 6 and replace with 9 and return the number

        # TC : O(N)
        # SC : O(N)
        
        num = str(num)
        for ind in  range (len(num)):
            if num[ind]=="6":
                return int(num[:ind] + "9" + num[ind+1:])

        return num
    
    
    def maximum69Number (self, num: int) -> int:

        # find first 6 and replace with 9 and return the number

        # TC : O(N)
        # SC : O(1)
        
        num_copy = num
        ind = -1
        pointer = 0

        while num_copy:
            if num_copy%10 == 6:
                ind = pointer
            num_copy //= 10
            pointer += 1
        
        return num if ind == -1 else num + 3 *(10**ind)