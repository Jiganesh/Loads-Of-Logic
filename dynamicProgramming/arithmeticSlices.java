
// https://leetcode.com/problems/arithmetic-slices/
// Solution : https://www.youtube.com/watch?v=qRHWAKCOLxM
package dynamicProgramming;


public class arithmeticSlices {

    public static void main(String[] args) {

        SolutionAS solution = new SolutionAS();
        System.out.println(solution.numberOfArithmeticSlices(new int[] {1,2,3,4}));
        System.out.println(solution.numberOfArithmeticSlices(new int[] {7,7,7,7,7}));

        
        System.out.println(solution.numberOfArithmeticSlicesApproach2(new int[] {1,2,3,4}));
        System.out.println(solution.numberOfArithmeticSlicesApproach2(new int[] {7,7,7,7,7}));
        
    }
    
}

class SolutionAS {

    // Submitted by Jiganesh

    //TC : O(N)
    //SC : O(N)


    // Runtime: 1 ms, faster than 23.94% of Java online submissions for Arithmetic Slices.
    // Memory Usage: 42.3 MB, less than 17.44% of Java online submissions for Arithmetic Slices.

    public int numberOfArithmeticSlices(int[] nums) {
        
        int [] dp = new int[nums.length+1];
        int total=0;
        
        for (int i=2; i<nums.length; i++){
            if (nums[i]-nums[i-1]==nums[i-1]-nums[i-2]){
                dp[i]+=dp[i-1]+1;
            }else{
                dp[i]=0;
            }
            
            total+= dp[i];
        }
        
        return total;
    }


    // Space Optimized

    // TC : O(N)
    // SC : O(1)

    // Runtime: 0 ms, faster than 100.00% of Java online submissions for Arithmetic Slices.
    // Memory Usage: 40 MB, less than 50.59% of Java online submissions for Arithmetic Slices.
    public int numberOfArithmeticSlicesApproach2(int[] nums) {
            
        int previousCount =0 ;
        int total=0;
        
        for (int i=2; i<nums.length; i++){
            if (nums[i]-nums[i-1]==nums[i-1]-nums[i-2]){
                previousCount+=1;
            }else{
                previousCount=0;
            }
            
            total+= previousCount;
        }
        
        return total;
    }

}
