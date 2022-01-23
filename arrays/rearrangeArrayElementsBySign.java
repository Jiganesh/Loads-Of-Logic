package arrays;

// https://leetcode.com/problems/rearrange-array-elements-by-sign/

import java.util.Arrays;

public class rearrangeArrayElementsBySign {
    public static void main(String[] args) {
        SolutionRAEBS solution = new SolutionRAEBS();
        System.out.println(Arrays.toString(solution.rearrangeArray(new int[]{3,1,-2,-5,2,-4})));
    }
    
}


class SolutionRAEBS {

    // Submitted by @Jiganesh

    // TC: O(N)
    // SC : O(1)

    // Runtime: 6 ms, faster than 60.00% of Java online submissions for Rearrange Array Elements by Sign.
    // Memory Usage: 92.4 MB, less than 60.00% of Java online submissions for Rearrange Array Elements by Sign.

    public int[] rearrangeArray(int[] nums) {
        
        int n = nums.length;
        int [] array = new int[n];
        int positivePointer =0,negativePointer =0;
        int arrayPointer=0;

        while(positivePointer< n || negativePointer < n){
            
            while(positivePointer<n && nums[positivePointer]<0){
                positivePointer++;
            }
            
            while(negativePointer<n && nums[negativePointer]>0){
                negativePointer++;
            }
            
            if (positivePointer<n) array[arrayPointer]=nums[positivePointer];
            arrayPointer++;
            
            if (negativePointer<n) array[arrayPointer]=nums[negativePointer];
            arrayPointer++;
            
            positivePointer++;
            negativePointer++;
        }
        
        return array;  
    }
}