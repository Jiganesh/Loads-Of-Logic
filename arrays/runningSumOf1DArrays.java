package arrays;

// https://leetcode.com/problems/running-sum-of-1d-array/
import java.util.Arrays;

public class runningSumOf1DArrays {
    public static void main(String[] args) {
        SolutionRSO1DA solution= new SolutionRSO1DA();
        System.out.println(Arrays.toString(solution.runningSum(new int [] {1,2,3,4}))); // [1,3,6,10]
        System.out.println(Arrays.toString(solution.runningSum(new int [] {1,1,1,1,1}))); // [1,2,3,4,5]

    }
    
}

class SolutionRSO1DA {
    public int[] runningSum(int[] nums) {
        int sum=0;
        
        for(int i =0; i<=nums.length-1; i++){
           nums[i] = sum+nums[i];
            sum = nums[i];
        }
        return nums;
    }
}
