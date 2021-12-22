package arrays;

import java.util.ArrayList;
import java.util.List;

public class addToArrayFormOfInteger {
    public static void main(String[] args) {
        SolutionATAFOI solution = new SolutionATAFOI() ;
        System.out.println(solution.addToArrayForm(new int[]{9,9,9,9,9,9,9,9,9,9}, 1));
        System.out.println(solution.addToArrayForm(new int[]{2,1,5}, 806));

        
    }
}

class SolutionATAFOI {
    public List<Integer> addToArrayForm(int[] num, int k) {
        List<Integer> res = new ArrayList<Integer> ();
        long result=k; 
        for (int i =0; i< num.length; i++){
            result +=  num[i]* Math.pow(10,num.length-i-1);
            //System.out.println(num[i]*Math.pow(10,num.length-i-1)+" "+ result); 
        }     

        System.out.println(result);
        while(result>0){
            int a = (int) result%10;
            res.add(0, a);
            result/=10;
        }
        return res;
    }
}
