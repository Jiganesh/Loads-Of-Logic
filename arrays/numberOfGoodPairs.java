package arrays;

import java.util.HashMap;
public class numberOfGoodPairs {
    public static void main(String[] args) {
        SolutionNOGP solution = new SolutionNOGP();
        System.out.println(solution.numIdenticalPairs(new int[]{1,2,3,1,1,3})); //4
        System.out.println(solution.numIdenticalPairs(new int[]{1,1,1,1})); //6
        System.out.println(solution.numIdenticalPairs(new int[]{1,2,3})); //0

        System.out.println(solution.numIdenticalPairsEfficientSolution(new int[]{1,2,3,1,1,3})); //4
        System.out.println(solution.numIdenticalPairsEfficientSolution(new int[]{1,1,1,1})); //6
        System.out.println(solution.numIdenticalPairsEfficientSolution(new int[]{1,2,3})); //0
       
    }
}

class SolutionNOGP{
    public int numIdenticalPairs(int[] nums) {

        //TC = O(N^2)
        //SC = O(1)

        int count =0;
        for (int i=0 ; i < nums.length; i++){
            for(int j = 0 ; j< nums.length ;j++){
                if(nums[i]==nums[j] && i<j) count++;
            }
        }
        return count;
    }

    //TC : O(N)
    //SC : O(N)
    public int numIdenticalPairsEfficientSolution(int[] nums){
        int count =0 ;
        HashMap<Integer, Integer> lookup = new HashMap<Integer, Integer>();
        for (int i : nums){
            if(lookup.containsKey(i)){
                int getKeyValue = lookup.get(i);
                count+= getKeyValue;
                lookup.put(i, getKeyValue+1 );
            }else{
                lookup.put(i, 1);
            }
        }
        return count;
    }
}