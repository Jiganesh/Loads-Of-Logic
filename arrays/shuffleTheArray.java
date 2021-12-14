package arrays;

import java.util.Arrays;

public class shuffleTheArray {
    public static void main(String[] args) {
        SolutionSTA solution = new SolutionSTA();
        System.out.println(Arrays.toString(solution.shuffle(new int[]{1,2,3,4,4,3,2,1}, 4))); //[2,3,5,4,1,7] 
        System.out.println(Arrays.toString(solution.shuffle(new int[]{2,5,1,3,4,7}, 3))); //[1,4,2,3,3,2,4,1]
        System.out.println(Arrays.toString(solution.shuffle(new int[]{1,1,2,2}, 2))); //[1,2,1,2]

    }    
}


class SolutionSTA {
    public int[] shuffle(int[] nums, int n) {
        int [] result = new int [nums.length];
        for(int i=0 ; i< n; i++){
            result[i*2]= nums[i];
            result[i*2+1]=nums[i+n];
        }
        return result;
    }
}