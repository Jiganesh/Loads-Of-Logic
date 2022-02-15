// https://leetcode.com/problems/single-number/
package bitManipulation;

public class singleNumber {

    public static void main(String[] args) {
        SolutionSN solution= new SolutionSN();
        System.out.println(solution.singleNumber(new int[]{2,2,1}));
        System.out.println(solution.singleNumber(new int[]{4,1,2,1,2}));
    }
    
}


class SolutionSN {

    // Submitted by @Jiganesh

    // TC : O(n)
    // SC : O(1)

    // Runtime: 0 ms, faster than 100.00% of Java online submissions for Single Number.
    // Memory Usage: 42.1 MB, less than 71.26% of Java online submissions for Single Number.

    public int singleNumber(int[] nums) {
        
        int a =0;
        for (int i =0 ; i< nums.length; i++){
            a^=nums[i];
        }
        return a;
        
    }
}