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


    //TC :O(2^n)
    //SC :O(n)
    // Using Recursion
    public int climbStairs(int n){
        return (n<=2) ? n : climbStairs(n-1) + climbStairs(n-2);
    }


    //TC :O(n)
    //SC :O(n)
    // Using DP and memoization
    public int climbStairsApproach2(int n) {
        
        if (n<=2) return n;
        int[] array = new int[n+1];
        array[0]=0;
        array[1]=1;
        array[2]=2;
        
        for (int i = 3 ; i<=n; i++){
            array[i]=array[i-1]+array[i-2];
        }
        
        return array[n]; 
            
    }
    
    // TC : O(N)
    // SC : O(1)

    // Modified Solution
    public int climbStairsApproach3(int n) {

        int a =1, b = 1;
        for (int i=2 ; i<=n; i++){
            int temp = a;
            a= b;
            b = temp +b;
        }
        return b;
        
    }
}