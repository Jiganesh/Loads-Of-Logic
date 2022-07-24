# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution(object):
    
    # Runtime: 64 ms, faster than 22.85% of Python online submissions for Search in Rotated Sorted Array II.
    # Memory Usage: 14 MB, less than 40.45% of Python online submissions for Search in Rotated Sorted Array II.
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def findPivot (nums):
            start  =0 
            end = len(nums)-1
            
            while start<= end :
                mid = start + (end-start)//2
                midElement = nums[mid]
                
                if ( mid<end and nums[mid]> nums[mid+1]): return mid
                if ( mid>start and nums[mid-1] > nums[mid]): return mid-1
                
                if (nums[start]== midElement and midElement == nums[end]):
                    
                    if (start<end and nums[start]>nums[start+1]): return start
                    start+=1
                    if (start < end and nums[end-1]>nums[end]) : return end-1
                    end-=1
                    
                elif (nums[start]< nums[mid] ) or (nums[start]==nums[mid]  and nums[mid]>nums[end]):
                    start=mid+1
                else :
                    end = mid-1
                    
                    
            return -1
        
        def binarySearch (nums, start, end ,target):
            while start <= end :
                mid = start+ (end -start)//2
                if nums[mid] == target : return True
                elif nums[mid]< target : start = mid+1
                else : end = mid-1
            return False
                
        
        
        pivot = findPivot(nums);
        if pivot != -1:
            if (target>= nums[0]):
                return binarySearch(nums, 0, pivot, target)
            else:
                return binarySearch(nums,pivot+1, len(nums)-1, target)
        else :
            return binarySearch (nums,0 , len(nums)-1, target)
        
