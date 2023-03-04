# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/


from typing import List
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:


        # check if it is possible to divide the array in three partitions
        sum = 0
        for i in arr:
            sum+= i
        
        if sum % 3 != 0:
            return False

        partition = sum//3
        partition_sum = 0
        number_of_partition = 0

        for num in arr:
            partition_sum += num
            if partition_sum == partition:
                number_of_partition +=1
                partition_sum = 0
        
        return number_of_partition >= 3 


        