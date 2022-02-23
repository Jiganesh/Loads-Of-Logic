package dynamicProgramming;

public class minCostClimbingStairs {
    public static void main(String[] args) {
        SolutionMCCS solution = new SolutionMCCS();
        System.out.println(solution.minCostClimbingStairs(new int[]{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}));
    }
    
}


class SolutionMCCS {

    // Submitted by @Jiganesh 

    // TC : O(N)
    // SC : O(N)

    // Runtime: 8 ms, faster than 5.48% of Java online submissions for Min Cost Climbing Stairs.
    // Memory Usage: 44.7 MB, less than 5.17% of Java online submissions for Min Cost Climbing Stairs.
    public int minCostClimbingStairs(int[] cost) {
        
        
        int[] dp = new int[cost.length];
        dp[0]= cost[0];
        dp[1]= cost[1];
        
        for (int i=2 ; i<cost.length;i++){
            dp[i] = cost[i]+Math.min(dp[i-1], dp[i-2]);
        }
        
        int n = dp.length;
        return Math.min(dp[n-1], dp[n-2]);
    }

    // Efficient Solution
    
    // TC : O(N)
    // SC : O(1)

    // Runtime: 1 ms, faster than 89.31% of Java online submissions for Min Cost Climbing Stairs.
    // Memory Usage: 43.8 MB, less than 15.27% of Java online submissions for Min Cost Climbing Stairs.

    public int minCostClimbingStairsApproach2(int[] cost) {
        
        int a= cost[0];
        int b= cost[1];
        
        for (int i=2 ; i<cost.length;i++){
            int temp = b;
            b = cost[i]+Math.min(a, b);
            a = temp;
        }
        
        return Math.min(a,b);
    }
}