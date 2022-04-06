# https://leetcode.com/problems/3sum-with-multiplicity/

class Solution:

    # TLE
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        
        count = 0
        for i in range (len(arr)-2):
            for j in range (i+1, len(arr)-1):
                for k in range (j+1 , len(arr)):
                    if i< j < k and arr[i]+arr[j]+arr[k]== target:
                        count+=1
        return count
    
    # TC : O(N^2)
    # SC : O(N)
    def threeSumMulti(self, A, target):
        MOD = 10**9 + 7
        count = collections.Counter(A)
        keys = sorted(count)

        ans = 0

        # Now, let's do a 3sum on "keys", for i <= j <= k.
        # We will use count to add the correct contribution to ans.
        for i, x in enumerate(keys):
            T = target - x
            j, k = i, len(keys) - 1
            while j <= k:
                y, z = keys[j], keys[k]
                if y + z < T:
                    j += 1
                elif y + z > T:
                    k -= 1
                else: # x+y+z == T, now calculate the size of the contribution
                    if i < j < k:
                        ans += count[x] * count[y] * count[z]
                    elif i == j < k:
                        ans += count[x] * (count[x] - 1) / 2 * count[z]
                    elif i < j == k:
                        ans += count[x] * count[y] * (count[y] - 1) / 2
                    else:  # i == j == k
                        ans += count[x] * (count[x] - 1) * (count[x] - 2) / 6

                    j += 1
                    k -= 1

        return ans % MOD
    
    
    # TC : O(N^2)
    # SC : O(1)   
    
    # Runtime: 4186 ms, faster than 31.98% of Python3 online submissions for 3Sum With Multiplicity.
    # Memory Usage: 14.1 MB, less than 22.67% of Python3 online submissions for 3Sum With Multiplicity.
    
    def threeSumMulti(self, A: List[int], target: int) -> int:
        
        MOD = 10**9 + 7
        ans = 0
        A.sort()

        for i, x in enumerate(A):
            # We'll try to find the number of i < j < k
            # with A[j] + A[k] == T, where T = target - A[i].

            # The below is a "two sum with multiplicity".
            T = target - A[i]
            j, k = i+1, len(A) - 1

            while j < k:
                # These steps proceed as in a typical two-sum.
                if A[j] + A[k] < T:
                    j += 1
                elif A[j] + A[k] > T:
                    k -= 1
                # These steps differ:
                elif A[j] != A[k]: # We have A[j] + A[k] == T.
                    # Let's count "left": the number of A[j] == A[j+1] == A[j+2] == ...
                    # And similarly for "right".
                    left = right = 1
                    while j + 1 < k and A[j] == A[j+1]:
                        left += 1
                        j += 1
                    while k - 1 > j and A[k] == A[k-1]:
                        right += 1
                        k -= 1

                    # We contributed left * right many pairs.
                    ans += left * right
                    ans %= MOD
                    j += 1
                    k -= 1

                else:
                    # M = k - j + 1
                    # We contributed M * (M-1) / 2 pairs.
                    # nC2
                    ans += (k-j+1) * (k-j) / 2
                    ans %= MOD
                    break

        return int(ans)
    

        