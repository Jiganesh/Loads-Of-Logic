# https://leetcode.com/problems/make-array-strictly-increasing/

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:

        arr2.sort()

        dp = {}
        n = len(arr1)
        m = len(arr2)


        def helper(prev, ind):

            if ind >= n:
                return 0

            if (prev, ind) in dp:
                return dp[(prev, ind)]

            greater_number_ind = bisect.bisect_right(arr2, prev)
            
            ans = float("inf")

            if prev < arr1[ind]:
                ans = min(ans, helper(arr1[ind], ind+1))

            if greater_number_ind < m:
                ans = min(ans, helper(arr2[greater_number_ind], ind+1)+1)
            
            dp[(prev, ind)] = ans
            return ans
            

        result = helper(-1, 0)
        return -1 if result == float("inf") else result


