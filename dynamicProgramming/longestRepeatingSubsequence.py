# https://www.codingninjas.com/codestudio/problems/longest-repeating-subsequence_1118110?leftPanelTab=1

def longestRepeatingSubsequence(s, n):

    # Write your code here
    # Return an integer denoting the length of the longest repeating subsequence
	s1= s
	s2 =s
	dp = [[0]*(len(s)+1) for i in range (len(s)+1)]
	for i in range (1,len(s1)+1):
		for j in range (1, len(s2)+1):
			if s1[i-1]== s2[j-1] and i!=j:
				dp[i][j] = 1 + dp[i-1][j-1]
			else :
				dp[i][j]= max(dp[i-1][j], dp[i][j-1])
	return dp[-1][-1]

print(longestRepeatingSubsequence("ABCAB",5))
print(longestRepeatingSubsequence("ABCBDCD", 7))