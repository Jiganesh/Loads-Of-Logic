class Solution:
    def minMaxGame(self, nums) -> int:
        
        while len(nums)>1:
            nums = [nums[i :i+2]  for i in range(0,len(nums),2)]
            array = []
            for index, i in enumerate(nums):
            
                if index%2==0:
                    array.append(min(i))
                else:
                    array.append(max(i))
            nums=array
        return nums[0]
    
    
print(Solution().minMaxGame([1,3,5,2,4,8,2,2])) #1
print(Solution().minMaxGame([3])) #3
print(Solution().minMaxGame([10,3,6,9])) #3
print(Solution().minMaxGame([10,12,4,3,4,3])) #3