# BruteForce
from tkinter import N


class Solution(object):
	def minimumTaxes(self, N, K, taxOfficers):
		houses = [float("inf")]*N
		for location, fixed_tax in taxOfficers:
			for i in range (N):
				houses[i] = min(houses[i], fixed_tax + abs(i-location))
		return houses

#Optimal Solution

class Solution(object):
	def minimumTaxes(self, N, K, taxOfficers):
		houses, taxOffice = [float("inf")]*N , [False]*N
  
		for index, fixed_tax in taxOfficers:
			houses[index] = fixed_tax
			taxOffice[index] = True

		left = float('inf')
		for i in range(N):
			if 	not taxOffice[i]:
				left+=1
				houses[i]= min(houses[i], left)
			else:
				left = min(left+1, houses[i])
    
		right = float('inf')
		for i in range(N-1, -1, -1):
			if not taxOffice[i]:
				right+=1
				houses[i]= min(houses[i], right)
			else:
				right = min(right+1, houses[i])
		return houses

print(Solution().minimumTaxes(8, 2, [[2,14], [6,16]]))
print(Solution().minimumTaxes(9, 2, [[0, 1], [8, 2]]))
print(Solution().minimumTaxes(6, 3, [[2, 3], [3, 4], [5, 8]]))
print(Solution().minimumTaxes(8, 4, [[2, 2],[3,5], [5,6], [7, 7]]))