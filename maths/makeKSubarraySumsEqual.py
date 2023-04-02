# https://leetcode.com/problems/find-the-substring-with-maximum-cost/

class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        

        '''
        [1,4,1,3]

        a. 1 + 4 = 5
        b.     4 + 1 = 5
        c.         1 + 3 = 4
        d.             3 + 1 = 4


        As from the above you can understand the num which goes in should be equal to number.
        
        In case b, 1 (index - 2) gets in the window  and 1 (index - 0) gets out which are same.
        In case c  3 (index - 3) gets in the window and 4 (index - 1) gets out which are not same.
        
        Hence we could have grouped them [1, 1] [3, 4] in these buckets and same they should be same to make subarray equal.

        As array is circular the step can be changed

        suppose k is 2

        [1, 4, 1, 3]
step 1   ^     ^ 

^ these are pointers now if the array is circular and you take the pointer skipping one element the pointers will end again on 1 and 1, gcd (4, 2) = 2 which means there will be 2 buckets and every number will be put in after skipping one.

bucket 1 = [1, 1]
bucket 2 = [3, 4]


        suppose k is 3

        [2, 5, 5, 7]
step 1   ^        ^
step 2      ^  ^

These where we use gcd to find buckets gcd (4, 3) = 1 which means there will be one bucket and every other number will be in it

bucket 1 =  [2, 5, 5, 7]


Now the simplest task making each bucket equal
- The optimal way to do this is use gready approach and use median to find minimum operations to make numbers equal

for example 1

bucket 2 = [4, 3]

median = sorted([4, 3]) = [3, 4] = 4
get absolute difference from all numbers in array which will be one (3 - 4) + (4 - 4) = 1


for example 2

median = sorted([2, 5, 5, 7]) = [2, 5, 5, 7] = 5
get absolute difference from all numbers in array which will be one (2 - 5) + (5 - 5) + (5 - 5)  + (7 - 5) = 5


        
        '''
        n = len(arr)

        no_of_buckets = gcd (k, n)
        buckets = defaultdict(list)

        for ind, num in enumerate(arr):
            buckets[ind % no_of_buckets].append(num)

        result = 0
        print(buckets)
        for bucket_number, bucket in buckets.items():
            sorted_bucket = sorted(bucket)
            m = len(sorted_bucket)
            median = sorted_bucket[(m)//2]
            print(median)
            
            for num in bucket:
                result += abs(median - num)

        return result
