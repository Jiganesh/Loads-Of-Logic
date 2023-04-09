# https://leetcode.com/problems/sum-of-distances/

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        index_prefix_sum = defaultdict(lambda: [0])
        occurences = defaultdict(int)
        
        for ind, num in enumerate(nums):
            index_prefix_sum[num].append(index_prefix_sum[num][-1]+ind)

        result = []
        
        for ind, num in enumerate(nums):
            occurences[num]+=1
            occurence = occurences[num]

            prefix_sum = index_prefix_sum[num]
            prefix_sum_index = occurence

            left_sum = prefix_sum[prefix_sum_index-1]
            right_sum = prefix_sum[-1] - prefix_sum[prefix_sum_index]

            numbers_on_left = prefix_sum_index - 1
            numbers_on_right = len(prefix_sum)-prefix_sum_index - 1

            abs_on_left = abs(left_sum - (numbers_on_left * ind))
            abs_on_right = abs(right_sum - (numbers_on_right * ind))

            total_abs = (abs_on_left + abs_on_right)
            result.append(total_abs)

        return result
         
        


            


        