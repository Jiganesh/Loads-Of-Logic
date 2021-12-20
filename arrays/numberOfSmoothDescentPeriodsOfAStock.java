package arrays;

import java.util.ArrayList;

public class numberOfSmoothDescentPeriodsOfAStock{
    public static void main(String[] args) {
        SolutionNOSDPOS solution = new SolutionNOSDPOS();
        System.out.println(solution.getDescentPeriods(new int[]{3,2,1,4 }));
        System.out.println(solution.getDescentPeriods(new int[]{8,6,7,7 }));
        System.out.println(solution.getDescentPeriods(new int[]{1 }));

        
    }
}


class SolutionNOSDPOS {

    // Wrong Solution
    public long getDescentPeriods(int[] prices) {

        //ArrayList <Integer> list = new ArrayList<>();
        int total = 0;
        int count =0;
        for (int i=0; i< prices.length; i++){
            if (i+1<prices.length && prices[i]-prices[i+1]==1 ){
                count+=1;
            }else {
                //list.add(count+1);
                total +=factorial(count+1);
                count=0;
            }
        }
        //System.out.println(list);
        return total;
    }

    public int factorial(int number){
        return (number <=1) ?1 : number*factorial(number-1);
    }
}