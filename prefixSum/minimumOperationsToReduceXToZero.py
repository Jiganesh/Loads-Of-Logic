# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

import operator
from itertools import accumulate

class Solution:


    # TLE

    # TC : O(N^2)
    # SC : O(N)
    def minOperations(self, nums, x) :

        middle_array = sum(nums)-x
        prefix_sum = [0]+list(accumulate(nums, operator.add))

        max_len=0
        for i in range (len(prefix_sum)):
            for j in range (i+1 , len(prefix_sum)):
                if prefix_sum[j]-prefix_sum[i] == middle_array:
                    max_len = max(max_len, j-i)

        if max_len == 0 and prefix_sum[-1]!=x: return -1

        return (len(nums)-max_len)

    # TC : O(N)
    # SC : O(N)
    def minOperations(self, nums, x):

        middle_array = sum(nums)-x
        prefix_sum = list(accumulate(nums, operator.add))

        lookup = {0:-1}

        max_len=0
        for i in range (len(prefix_sum)):

            if prefix_sum[i]-middle_array in lookup :
                max_len = max(max_len, i - lookup[prefix_sum[i]-middle_array])

            lookup[prefix_sum[i]]= i

        if max_len == 0 and prefix_sum[-1]!=x: return -1
        return (len(nums)-max_len)















'''
# TESTCASES

[1,1,4,2,3]
5
[5,6,7,8,9]
4
[3,2,20,1,1,3]
10
[1,1,1,1,9,9,6]
10
[8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309]
134365
'''