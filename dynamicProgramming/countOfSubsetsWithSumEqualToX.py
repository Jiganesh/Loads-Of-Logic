

class Solution:

	# TopDownApproach
	def countOfSubsetsWithSumEqualToX(self, arr, X):

		dp = [[0 for i in range(X+1)] for i in range(len(arr)+1)]

		for i in range(len(arr)+1):
			for j in range(X+1):
				if i == 0:
					dp[i][j] = 0
				if j == 0:
					dp[i][j] = 1

		for i in range(1, len(arr) + 1):
			for j in range( X+1):   # we just dont start fron 1 because in case there is zero in between 1 changes to 2
				if arr[i-1] <= j:
					dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
				else:
					dp[i][j] = dp[i-1][j]


		for i in dp:
			for j in i:
				print(j,  end="  ")
			print()

		return dp[len(arr)][X]

	# Recursion Approach

	def countOfSubsetsWithSumEqualToX(self, arr, X):

		def helper(arr, X, idx):
			if X == 0:
				return 1
			res = 0
			if X > 0:
				for i in range(idx, len(arr)):
					res += helper(arr, X-arr[i], i+1)
			return res
		return helper(arr, X, 0)


print(Solution().countOfSubsetsWithSumEqualToX([1, 1 ,1 ,1 ], 1))  # 4
# print(Solution().countOfSubsetsWithSumEqualToX([1, 2, 3, 3], 6))  # 3
# print(Solution().countOfSubsetsWithSumEqualToX([4, 3, 2, 3, 5, 2, 1], 5))  # 7
# print(Solution().countOfSubsetsWithSumEqualToX([2, 3, 5, 6, 8, 10], 10))  # 3
# print(Solution().countOfSubsetsWithSumEqualToX([1, 2, 3, 4, 5], 7))  # 3
# print(Solution().countOfSubsetsWithSumEqualToX([9, 7, 0, 3, 9, 8, 6, 5, 7, 6], 31)) 
