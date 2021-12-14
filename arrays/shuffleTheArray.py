
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        
        array = []
        for i in range (n):
            array.append(nums[i])
            array.append(nums[i+n])
        return array;
    
    
        # One liner solution
        # return [j for i in range(n) for j in (nums[i], nums[i+n])]
    
        ''' One liner Explanation'''
        
        '''
        
        for i in range(n):
            for j in (nums[i], nums[i+n]):
                print(j)
        '''
    
    

    
print(Solution.shuffle(Solution, [2,5,1,3,4,7], 3))
    
