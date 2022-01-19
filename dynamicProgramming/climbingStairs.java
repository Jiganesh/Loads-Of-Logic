package dynamicProgramming;

// https://leetcode.com/problems/climbing-stairs/
public class climbingStairs {
    public static void main(String[] args) {

        SolutionCS solution  = new SolutionCS();
        System.out.println(solution.climbStairs(38));
    
    }
}

class SolutionCS {

    // Submitted by @Jiganesh
    
    // TC : O(N)
    // SC : O(1)
    public int climbStairs(int n) {

        int a =1, b = 1;
        for (int i=2 ; i<=n; i++){
            int temp = a;
            a= b;
            b = temp +b;
        }
        return b;
        
    }
}