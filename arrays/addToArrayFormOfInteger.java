package arrays;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class addToArrayFormOfInteger {
    public static void main(String[] args) {
        SolutionATAFOI solution = new SolutionATAFOI() ;
        System.out.println(solution.addToArrayForm(new int[]{9,9,9,9,9,9,9,9,9,9}, 1));
        System.out.println(solution.addToArrayForm(new int[]{2,1,5}, 806));
        System.out.println(solution.addToArrayForm(new int[]{1,2,0,0}, 34));
        System.out.println(solution.addToArrayForm(new int[]{2,7,4}, 181));        
    }
}

class SolutionATAFOI {

    //41 ms using ArrayList
    public List<Integer> addToArrayForm(int[] num, int k) {
        List<Integer> res = new ArrayList<Integer> ();
        int i = num.length-1;
        while(k>0 ||  i>=0){

            int add  = (i>=0)?k+num[i]:k+ 0;
            res.add(0,add%10 ); //41 ms because of this step
            k=add/10;
            i--;
        }
        return res;
    }

    // 3ms using LinkedList but inserting at first and not using optimized addFirst
    public List<Integer> addToArrayFormApproach2(int[] num, int k) {
        List<Integer> res = new LinkedList<Integer> ();
        int i = num.length-1;
        while(k>0 ||  i>=0){

            int add  = (i>=0)?k+num[i]:k+ 0;
            res.add(0,add%10 ); //3 ms because of this step
            k=add/10;
            i--;
        }
        return res;
    }

    //Using LinkedList in such situation is much more effcient with addFirst
    public List<Integer> addToArrayFormApproach3(int[] num, int k) {
        LinkedList<Integer> res = new LinkedList<Integer> ();
        int i = num.length-1;
        while(k>0 ||  i>=0){

            int add  = (i>=0)?k+num[i]:k+ 0;
            res.addFirst(add%10 ); //2 ms because of this step
            k=add/10;
            i--;
        }
        return res;
    }
}
