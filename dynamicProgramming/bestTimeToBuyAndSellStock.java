package dynamicProgramming;

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
// Solution : https://www.youtube.com/watch?v=4YjEHmw1MX0


public class bestTimeToBuyAndSellStock {
    public static void main(String[] args) {
        
    }
}


class Solution {

    
    // TC : O(N^2
    // SC : O(1)

    //Brute Force
    public int maxProfit(int[] prices) {

        int maxProfit = 0;

        for (int i = 0 ; i< prices.length ; i++){
            for (int j = i ; j < prices.length; j++){
                maxProfit = Math.max(maxProfit,prices[j]- prices[i]);
            }
        }
        return maxProfit;
    }

    // TC : O(N)
    // SC : O(1)

    // Runtime: 2 ms, faster than 78.41% of Java online submissions for Best Time to Buy and Sell Stock.
    // Memory Usage: 52.1 MB, less than 69.52% of Java online submissions for Best Time to Buy and Sell Stock.

    public int maxProfitApproach2(int[] prices) {

        int leastStockSoFar= prices[0];
        int maxProfit = 0;

        for (int i: prices){
            leastStockSoFar = Math.min(i, leastStockSoFar);
            maxProfit = Math.max(maxProfit, i-leastStockSoFar);
        }
        return maxProfit;
    }
}