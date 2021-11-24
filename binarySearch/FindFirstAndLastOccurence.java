// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

package binarySearch;
import java.util.Arrays;

public class findFirstAndLastOccurence {
    public static void main(String[] args) {
        int[] array = new int[]{5,7,7,8,8,10};
        int target = 8;
        SolutionFFALO solution = new SolutionFFALO();
        System.out.println(Arrays.toString(solution.searchRange(array, target)));
        
    }
}
class SolutionFFALO {
    public int[] searchRange(int[] array, int target) {
        
        if(array.length==0) return new int[]{-1,-1};
        int start =0,end = array.length-1,pos=-1;
        while(start<=end){
            
            int mid = start +(end-start)/2;
            if(array[mid]<target) start = mid +1;
            else if(array[mid]>target) end =mid-1;
            else {start = end = pos =mid ; break;}
        }
        if (pos == -1) return new int[]{-1,-1};

        while(start>=0 && array[start]==target) start--;
        while(end<=array.length-1 && array[end]==target) end++;

        return new int[]{start+1,end-1};
        
    }
}