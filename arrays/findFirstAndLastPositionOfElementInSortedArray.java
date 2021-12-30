package arrays;

import java.util.Arrays;

public class findFirstAndLastPositionOfElementInSortedArray{
    public static void main(String[] args) {
        SolutionFFALPOEISA solution = new SolutionFFALPOEISA();
        int[] result =solution.searchRange(new int[]{5,7,7,8,8,10}, 8);
        System.out.println(Arrays.toString(result));   
        int[] result1 =solution.searchRange(new int[]{1,2,3,3,3,3,4,5,9}, 3);
        System.out.println(Arrays.toString(result1));   
        int[] result2 =solution.searchRange(new int[]{}, 1);
        System.out.println(Arrays.toString(result2));   
    }
}

class SolutionFFALPOEISA {
    public int[] searchRange(int[] nums, int target) {

        int start =0;
        int end = nums.length-1;
        int pos = -1;
        while(start<=end){
            int mid = start+(end-start)/2;
            if( nums[mid]<target) start = mid+1;
            else if (nums[mid]>target) end = mid-1;
            else {
                pos=start=end=mid;
                break;
            }
        }
        if (pos ==-1) return new int[]{-1,-1};
        while(start>=0 && nums[start]==nums[pos])start--;
        while(end<nums.length && nums[end]==nums[pos])end++;

        
        return new int[]{start+1,end-1};
        
    }
}