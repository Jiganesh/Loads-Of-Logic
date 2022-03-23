# https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1#

# Renamed count of subsets with sum equals to k


#User function Template for python3
class Solution:
    def perfectSum(self, arr, n, X):
        # code here
        
        dp = [[0 for i in range(X+1)] for i in range(len(arr)+1)]

        for i in range(len(arr)+1):
            for j in range(X+1):
                if i == 0:
                    dp[i][j] = 0
                if j == 0:
                    dp[i][j] = 1

        for i in range(1, len(arr) + 1):
            for j in range(X+1):
                if arr[i-1] <= j:
                    dp[i][j] = (dp[i-1][j] + dp[i-1][j-arr[i-1]]) %1000000007
                else:
                    dp[i][j] = dp[i-1][j] % 1000000007


        # Uncomment to view dp array

        # for i in dp:
        #     for j in i:
        #         print(j,  end="\t")
        #     print()

        return dp[len(arr)][X]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n,sum = input().split()
        n,sum = int(n),int(sum)
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.perfectSum(arr,n,sum)
        print(ans)

# } Driver Code Ends