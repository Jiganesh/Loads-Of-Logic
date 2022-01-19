package dynamicProgramming;

// https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

public class numberOfSmoothDescentPeriodsOfAStock{
    public static void main(String[] args) {

        SolutionNOSDPOAS solution = new SolutionNOSDPOAS();
        System.out.println(solution.getDescentPeriods(new int [] {3,2,1,4}));
        
    }
}

class SolutionNOSDPOAS{

    // Submitted by @Jiganesh

    // TC : O(N)
    // SC : O(1)
    public long getDescentPeriods(int[] prices) {
        long start=0, val=1;
        for (int i =1 ; i< prices.length; i++){
            if(prices[i-1]-prices[i]==1){
                val += i-start+1;
            }else{
                start=i;
                val+=1;
            }
        }
        return val;        
    }
    
    /* Example


    prices = [3,2,1,4]

    0       1           2           3
    
    3       2           1           4
    [3]     [2]         [1]         [4]
            [3,2]       [2,1]
                        [3,2,1]

    nextCount = previous + end - start + 1
    
    
    */

    
}