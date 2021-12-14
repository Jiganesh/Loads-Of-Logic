package arrays;

public class richestCustomerWealth {
    public static void main(String[] args) {
        SolutionRCW solution = new SolutionRCW();
        System.out.println(solution.maximumWealth(new int[][] {{1,5}, {7,3 },{3,5}}));
        
    }   
}

class SolutionRCW {
    public int maximumWealth(int[][] accounts) {
        int max = 0,sum =0;
        for (int people = 0 ; people <= accounts.length -1;people ++){
            sum =0;
            for (int account =0; account <= accounts[people].length-1; account++){
                sum += accounts[people][account];   
            }
            if (sum>max) max = sum;
        }
        return max;
    }
}