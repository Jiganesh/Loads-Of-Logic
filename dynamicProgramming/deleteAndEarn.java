// https://leetcode.com/problems/delete-and-earn/
// Solution https://www.youtube.com/watch?v=qVfjmkL1naw
package dynamicProgramming;



public class deleteAndEarn {
    public static void main(String[] args) {
        
    }
    
}


class SolutionDAE {

    // Submitted by Jiganesh

    // TC: O(N)
    // SC: O(N)

    // Runtime: 1 ms, faster than 100.00% of Java online submissions for Delete and Earn.
    // Memory Usage: 41.3 MB, less than 81.79% of Java online submissions for Delete and Earn.

    public int deleteAndEarn(int[] nums) {
        int maxNumber = 0;
        for (int i : nums){
            maxNumber = Math.max(i, maxNumber);
        }
        
        
        int [] dp = new int[maxNumber+1];
        int include =0, exclude = 0;
        
        for (int i: nums){
            dp[i]++;
        }
        
        
        for (int i=0; i<= maxNumber; i++){
            int temp = include ;
            include = dp[i]*i+ exclude;
            exclude = Math.max(exclude , temp);
        }
        
        return Math.max(include , exclude);
        
    }
}