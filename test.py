def helper (amount,cost1, cost2 ):
    
    dp = [0]*(amount+1)
    dp[0]=1
    
    for i in [cost1, cost2]:
        for j in range(1, amount+1):
            if i <=j:
                dp[j] = dp[j]+dp[j-i]

    return sum(dp)

print(helper(5,10,10))
print(helper(20, 10, 5))


