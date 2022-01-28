#https://leetcode.com/problems/lexicographical-numbers/

def lexicalOrder(n):
    
    
    # Runtime: 80 ms, faster than 99.69% of Python3 online submissions for Lexicographical Numbers.
    # Memory Usage: 19.9 MB, less than 96.30% of Python3 online submissions for Lexicographical Numbers.

    #lexicographical order focuses on the initial values and their weight instead of length of number
    #so 10000 is below 12 as 0 is less than 2
    #so the values like 12 2434 23 1 654 222 56 10000
    #will be orderd to  1 10000 12 222 23 2434 56 654
    #this can be done by converting to string and then sorting the numbers
    #so output will be like alphabetical like where 222 is below 23.

    nums=[i for i in range(1,n+1)]
    nums.sort(key=str)
    return nums

    #but this will also work 

    return sorted(str(i) for i in range(1,n+1))

print(lexicalOrder(13))