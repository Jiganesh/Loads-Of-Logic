# https://leetcode.com/problems/palindrome-partitioning/

class Solution(object):
	
	# Runtime: 582 ms, faster than 97.87% of Python online submissions for Palindrome Partitioning.
	# Memory Usage: 32.8 MB, less than 26.50% of Python online submissions for Palindrome Partitioning.   
	
	def partition(self, s):
		"""
		:type s: str
		:rtype: List[List[str]]
		"""
		result =[]
		
		def palindrome(s, i, j):
			a = s[i:j]
			return a==a[::-1]
		
		def helper (s, i, array=[], result=[]):
			
			if i==len(s):
				result.append(array[:])
				return 
			
			for k in range (i+1, len(s)+1):
				
				if palindrome(s, i, k):
					array.append(s[i:k])
					helper(s, k, array, result)
					array.pop()
			return result
					
		
		return helper(s, 0)