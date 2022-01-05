package arrays;

public class houseRobber{
    public static void main(String[] args) {
        SolutionHR solution = new SolutionHR ();
        System.out.println(solution.rob(new int[]{1,1,3,1,1,100}));
        System.out.println(solution.rob(new int[] {1,2,3,1}));
        System.out.println(solution.rob(new int[] {2,7,9,3,1}));
    }
}
class SolutionHR {
    public int rob(int[] nums) {
        if (nums.length ==0) return 0;
        int[] dp = new int [nums.length+1];
        dp[1]= nums[0];

        for (int i=1; i< nums.length; i++){
            dp[i+1] = (dp[i] > dp[i-1]+nums[i])?dp[i]:dp[i-1]+nums[i];
        }
        return dp[nums.length];
        
    }
}