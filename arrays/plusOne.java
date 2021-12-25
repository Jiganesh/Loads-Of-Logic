package arrays;

import java.util.Arrays;
import java.util.LinkedList;

public class plusOne {
    public static void main(String[] args) {
        SolutionPO solution = new SolutionPO();
        System.out.println(Arrays.toString(solution.plusOne(new int[]{9})));
        System.out.println(Arrays.toString(solution.plusOne(new int[]{1,2,3})));
        System.out.println(Arrays.toString(solution.plusOne(new int[]{4,3,2,1})));

    }
    
}

class SolutionPO {
    public int[] plusOne(int[] digits) {
        LinkedList <Integer> result = new LinkedList<Integer>();
        int n = digits.length-1;
        int k =1;
        while(k>0 || n>=0){
            int add = (n>=0)? digits[n]+k: k;
            result.addFirst(add %10);
            k = add /10;
            n--;
        }
        
        int [] res = new int[result.size()];
        for(int i = 0 ; i< res.length; i++){
            res[i] = result.get(i);
        }
        return res;
        
    }
}