// https://leetcode.com/problems/build-array-from-permutation/
 
package arrays;

import java.util.Arrays;

public class buildArrayFromPermutation {
    public static void main(String[] args) {
        SolutionBAFP solution = new SolutionBAFP();
        System.out.println(solution.buildArraySpaceEfficient(new int[]{5,0,1,2,3,4}));
        System.out.println(solution.buildArray(new int[]{0,2,1,5,3,4}));
    }
    
}


class SolutionBAFP {

    //TC : O(n)
    //SC : O(n)
    public int[] buildArray(int[] nums) {
        int [] result = new int[nums.length];
        for (int i =0 ; i<= nums.length-1; i++){
            result[i] = nums[nums[i]];
        }
        return result;
    }

    public int[] buildArraySpaceEfficient(int[] nums) {
        /*
        We can use this formula only when numbers are distinct and 1 to N (for this problem)
        It is more like Hashing
        As long as n is greater than max(array) and multiplication with n and stuff remains in range this will work;
        */
        int n = nums.length;
        for (int i =0 ; i<= nums.length-1; i++){
            nums[i] = n* (nums[nums[i]]%n) +nums[i];
        }
        
        for (int i =0 ; i<= nums.length-1; i++){
            nums[i] =nums[i]/n;
        }
        
        System.out.println(Arrays.toString(nums));
        return nums;
    }
}

/*

Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]
Explanation: The array ans is built as follows: 
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]


Input: nums = [5,0,1,2,3,4]
Output: [4,5,0,1,2,3]
Explanation: The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
    = [4,5,0,1,2,3]
*/
