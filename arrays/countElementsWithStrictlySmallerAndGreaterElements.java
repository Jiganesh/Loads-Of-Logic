package arrays;

// https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

import java.util.Arrays;

public class countElementsWithStrictlySmallerAndGreaterElements {
    public static void main(String[] args) {
        SolutionCEWSSAGE solution = new SolutionCEWSSAGE();
        System.out.println(solution.countElements(new int[]{11,7,2, 13}));
        
    }   
}

class SolutionCEWSSAGE {

    // TC : O(N)
    // SC : O(1)
    public int countElements(int[] nums) {

        int minimum = Arrays.stream(nums).min().getAsInt();
        int maximum = Arrays.stream(nums).max().getAsInt();

        int count =0;
        for (int i : nums){
            if (minimum< i && i < maximum){
                count++;
            }
        }
        return count;
        
    }
}