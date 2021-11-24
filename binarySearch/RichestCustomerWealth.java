// https://leetcode.com/problems/richest-customer-wealth/

package binarySearch;
class SolutionRichestCustomerWealth {
    public int maximumWealth(int[][] accounts) {
        int max = Integer.MIN_VALUE;
        int total =0;
        for (int person=0 ; person< accounts.length; person++){
            total = 0;
            for (int bank =0 ; bank < accounts[person].length; bank++){
                total+= accounts[person][bank];
            }
            if (total > max) max = total;
        }
        return max;
    }
}

public class richestCustomerWealth {
    public static void main(String[] args) {
        SolutionRichestCustomerWealth solution = new SolutionRichestCustomerWealth();
        int[][] accounts = {{1,2,3},{3,4,5},{3,4,5}};
        System.out.println(solution.maximumWealth(accounts));
        
    }
}
