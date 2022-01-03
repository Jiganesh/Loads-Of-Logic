#https://leetcode.com/problems/richest-customer-wealth/

def maximumWealth(accounts):

    #one liner
    # return max(sum(i) for i in accounts)

    maxx=0
    for i in accounts:
        #both below are equivalent
        
        # maxx= max(maxx, sum(i))
        maxx= maxx if (maxx> sum(i)) else sum(i)
    return maxx

#input
accounts = [[1,2,3],[3,2,1]]
print(maximumWealth(accounts))