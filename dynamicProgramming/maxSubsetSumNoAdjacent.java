// https://practice.geeksforgeeks.org/problems/max-sum-without-adjacents2430/1

package dynamicProgramming;

public class maxSubsetSumNoAdjacent {
    public static void main(String[] args) {
        
    }
}


class SolutionMSSNA {


    // TC : O(N)
    // SC : O(N)
    
    public int findMaxSum(int arr[], int n) {
         // code here
         if(n==0)
             return 0;
         if(n==1)
             return arr[0];
        
         int dp[] = new int[n];
         
         dp[0] = arr[0];
         dp[1] = Math.max(arr[0], arr[1]);
         
         for(int i=2 ; i<n ; i++){
             dp[i] = Math.max(dp[i-1] , dp[i-2] + arr[i]);
         }
         return dp[n-1];
    }

    // TC: O(N)
    // SC: O(1)
    public int findMaxSumApproach2(int arr[], int n) {

        if (n==0) return 0;
        if (n==1) return arr[0];


        int first=arr[0];
        int second=Math.max(arr[0],arr[1]);

        for (int i =2 ; i<n; i++){
            int current = Math.max(second , first+arr[i]);
            first = second;
            second = current;
        }

        return second;

    }


 }