#https://leetcode.com/problems/smallest-integer-divisible-by-k/

def smallestRepunitDivByK(k):
    
    #Brute force
    #first of all any number with 1 will not be divided with 2 or 5.
    #then, until we get divided by k generate number with all 1s and return its length
    
    # n=1
    # if k%2==0 or k%5==0:
    #     return -1
    # while(True):
    #     if n%k==0:
    #         return len(str(n))
    #     n=n*10+1
    
    
    #Improved Solution:
    
    # when we observed the formula n= n*10+1 and taking modulo with k to check its equal to 0
    # ie n= (n*10+1)%k
    # now, lets split what is n, n=k*quo+ rem
    # now, 10*n+1 = (10* (k*quo+rem) +1) %k --> (10*k*quo + 10*rem+ 1)%k
    # but as k*something is divisible by k, 10*k*quo will be cancelled
    # so value will depend on 10*rem+1 and can be calculated on
    # rem=(10*rem+1)%k
    
    
    n=1
    if k%2==0 or k%5==0:
        return -1
    rem=0
    for i in range(1, k+1):
        rem=(rem*10+1)%k
        if not rem:
            return i
    return -1

k= 3
print(smallestRepunitDivByK(k))