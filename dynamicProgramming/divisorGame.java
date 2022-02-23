// https://leetcode.com/problems/divisor-game/
// Solution : https://www.youtube.com/watch?v=1UW3SxuITKs

package dynamicProgramming;

import java.util.*;

public class divisorGame{
    public static void main(String[] args) {
        SolutionDG solution = new SolutionDG();
        System.out.println(solution.divisorGame(2));
        System.out.println(solution.divisorGame(3));
        System.out.println(solution.divisorGame(15));
        System.out.println(solution.divisorGame(24));

        System.out.println(solution.divisorGameApproach2(2));
        System.out.println(solution.divisorGameApproach2(3));
        System.out.println(solution.divisorGameApproach2(15));
        System.out.println(solution.divisorGameApproach2(24));

    }
}

class SolutionDG {

    // Submitted by @Jiganesh

    //TC: O(2^n)
    //SC: O(n)

    // TLE
    public boolean divisorGame(int n) {
        
        if (n<=1) return false;
        
        for (int i =1 ; i<=n/2; i++){
            if (n%i==0){
                if (! divisorGame(n-i)){
                    return true; 
                }
            }
        }
        
        return false;
        
    }

    //TC: O(n^2)
    //SC: O(n)

    // Runtime: 5 ms, faster than 16.79% of Java online submissions for Divisor Game.
    // Memory Usage: 41.2 MB, less than 10.38% of Java online submissions for Divisor Game.

    public boolean divisorGameApproach2(int n) {
        Object [] dp = new  Object[n+1];
        Arrays.fill(dp, null);
        dp[0]=false;
        dp[1]=false;
        return canWin(n, dp);
        
    }
    
    public boolean canWin(int n , Object[] dp){
        
        if (dp[n] != null) return (boolean)dp[n];
        
        for (int i =1 ; i<=n/2; i++){
            if (n%i==0){
                if (! canWin(n-i, dp)){
                    dp[n]=true;
                    return true; 
                }
            }
        }
        dp[n]=false;
        return false;
    }



    //TC :O(1)
    //SC :O(1)

    // Runtime: 0 ms, faster than 100.00% of Java online submissions for Divisor Game.
    // Memory Usage: 40.5 MB, less than 30.74% of Java online submissions for Divisor Game.

    public boolean divisorGameApproach3(int n) {


        // Math Proof explained in the video Please Watch OnceK
        
        return n%2==0;
        
    }
}