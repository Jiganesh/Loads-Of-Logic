package search;

// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

public class findMinimumInRotatedSortedArray {
    public static void main(String[] args) {
        SolutionFMIRSA solution = new SolutionFMIRSA();
        System.out.println(solution.findMin(new int[]{3,4,5,1,2}));
        System.out.println(solution.findMin(new int[]{4,5,6,7,0,1,2}));
        System.out.println(solution.findMin(new int[]{11,13,15,17}));
    }
}

class SolutionFMIRSA {
    public int findMin(int[] nums) {
        return nums[findPivot(nums)+1];
    }

    public int findPivot (int [] array){
        int start = 0;
        int end= array.length-1;
        
        while(start<=end){
            int mid = start + (end -start)/2;
            if (mid< end && array[mid]> array[mid+1]) return mid;
            if( mid >start && array[mid-1]> array[mid]) return mid-1;
            
            if (array[start]<=array[mid]) start = mid+1;
            else end = mid-1;
        }
        return -1;
    }
}