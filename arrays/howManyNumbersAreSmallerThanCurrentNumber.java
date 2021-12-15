package arrays;

import java.util.Arrays;

public class howManyNumbersAreSmallerThanCurrentNumber{
    public static void main(String[] args) {
        SolutionHMNASTCN solution = new SolutionHMNASTCN();
        System.out.println(Arrays.toString(solution.smallerNumbersThanCurrent(new int[]{8,1,2,2,3}))); // [4,0,1,1,3]
        
    }
}

class SolutionHMNASTCN{
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int [] result= new int[nums.length];
        
        for (int i =0 ; i< nums.length; i++){
            int count=0;
            for (int j = 0 ; j<nums.length; j++){
                if(i!=j && nums[j]< nums[i]) count++;
            }
            result[i]= count;
        }
        return result;
        
    }
}