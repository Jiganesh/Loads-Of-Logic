// https://www.youtube.com/watch?v=RyBM56RIWrM
package dynamicProgramming;

import java.util.Arrays;

public class countingBits{
    public static void main(String[] args) {
        SolutionCB solution = new SolutionCB ();
        System.out.println(Arrays.toString(solution.countBits(18)));
        System.out.println(Arrays.toString(solution.countBits(5)));
        System.out.println(Arrays.toString(solution.countBits(2)));

    }
}



class SolutionCB {


    // Submitted by Jiganesh

    // TC: O(NLogN);
    // SC : O(N);

    // Runtime: 4 ms, faster than 38.68% of Java online submissions for Counting Bits.
    // Memory Usage: 46.2 MB, less than 53.77% of Java online submissions for Counting Bits.
    
    public int[] countBits(int n) {
        
        int[] result = new int[n+1];
        
        for (int i = 0; i<=n; i++){
            result[i] = calculatebit(i);
        }
        
        return result;
    }
    
    public int calculatebit (int n ){
        
        int count =0;
        
        while (n !=0){
            if ((n&1) == 1) count+=1;
            n =n>>1;
        }
        
        return count;
    }
    
    // TC : O(N)
    // SC : O(N)

    // Runtime: 2 ms, faster than 82.30% of Java online submissions for Counting Bits.
    // Memory Usage: 47.8 MB, less than 39.71% of Java online submissions for Counting Bits.
    public int[] countBitsApproach2(int n) {
        
        int [] dp = new int[n+1];
        
        
        dp[0]=0;
        int count =1;
    
    
        for (int i = 1; i<=n; i++){
            
            if (2*count== i) count=i;
            dp[i]=1+dp[i-count];
              
        }
        
        return dp;
    }
}

