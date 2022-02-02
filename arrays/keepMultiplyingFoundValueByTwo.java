package arrays;

import java.util.Arrays;

public class keepMultiplyingFoundValueByTwo{
    public static void main(String[] args) {
        SolutionKMFVBT solution = new SolutionKMFVBT();
        System.out.println(solution.findFinalValue(new int[]{5,3,6,1,12}, 3)); // 24

        // Input: nums = [5,3,6,1,12], original = 3
        // Output: 24
        // Explanation: 
        // - 3 is found in nums. 3 is multiplied by 2 to obtain 6.
        // - 6 is found in nums. 6 is multiplied by 2 to obtain 12.
        // - 12 is found in nums. 12 is multiplied by 2 to obtain 24.
        // - 24 is not found in nums. Thus, 24 is returned.
        
        System.out.println(solution.findFinalValue(new int[]{6,5,3,1,12}, 3)); // 24

    }
}

class SolutionKMFVBT {
    public int findFinalValue(int[] nums, int original) {
        Arrays.sort(nums);
        
        for (int i : nums){
            if (i==original) original *=2;
        }
        return original;
    }
}