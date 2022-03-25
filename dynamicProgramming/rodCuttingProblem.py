# Question : https://www.codingninjas.com/codestudio/problems/rod-cutting-problem_800284

# 1225 ms
def cutRod(price, n):
	
	lengthOfRod = n
	lengths = [i for i in range (1,n+1)]
	lengthAndPrice = list(zip(lengths, price))
	
	dp = [[0]* (lengthOfRod+1) for i in range (len(lengthAndPrice)+1)]
	
	for i in range (1,len(lengthAndPrice)+1):
		for j in range (1,lengthOfRod+1):
			if lengthAndPrice[i-1][0]  <= j :
				dp[i][j] = max(dp[i-1][j], dp[i][j-lengthAndPrice[i-1][0]] + lengthAndPrice[i-1][1])
			else:
				dp[i][j] = dp[i-1][j] 
				
	# Uncomment Below Code to see DP Chart
	# for i in dp:print(*i)
		
	return dp[-1][-1]


# Little Optimization saving space using length-1 insted of zipping lengths with price


# 1005 ms
def cutRod(price, n):
	lengthOfRod = n
 	
	dp = [[0]* (lengthOfRod+1) for i in range (len(price)+1)]
	
	for i in range (1,len(price)+1):
		for length in range (1,lengthOfRod+1):
			if i <= length :
				dp[i][length] = max(dp[i-1][length], dp[i][length-i] + price[i-1])
			else:
				dp[i][length] = dp[i-1][length]
	return dp[-1][-1]




print(cutRod([2,5, 7, 8, 10],5)) #12
print(cutRod([3, 5, 8, 9, 10, 17, 17, 20], 8)) #24
print(cutRod([42, 68,35,1,70], 5)) #210
print(cutRod([25,79,59,63,65,6,46,82],8)) #316


# Test Code on Coding Ninjas



