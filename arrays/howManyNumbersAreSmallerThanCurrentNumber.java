package arrays;

import java.util.Arrays;
import java.util.HashMap;

public class howManyNumbersAreSmallerThanCurrentNumber{
    public static void main(String[] args) {
        SolutionHMNASTCN solution = new SolutionHMNASTCN();
        System.out.println(Arrays.toString(solution.smallerNumbersThanCurrent(new int[]{8,1,2,2,3}))); // [4,0,1,1,3]
        System.out.println(Arrays.toString(solution.smallerNumbersThanCurrentApproach2(new int[]{8,1,2,2,3}))); // [4,0,1,1,3]
        System.out.println(Arrays.toString(solution.smallerNumbersThanCurrentApproach3(new int[]{8,1,2,2,3}))); // [4,0,1,1,3]

        System.out.println(Arrays.toString(solution.smallerNumbersThanCurrent(new int[]{5,0,10,0,10,6}))); // [4,0,1,1,3]
        System.out.println(Arrays.toString(solution.smallerNumbersThanCurrentApproach2(new int[]{5,0,10,0,10,6}))); // [4,0,1,1,3]
        System.out.println(Arrays.toString(solution.smallerNumbersThanCurrentApproach3(new int[]{5,0,10,0,10,6}))); // [4,0,1,1,3]

    }
}

class SolutionHMNASTCN{

    //TC : O(N^2)
    //SC : O(N)
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

    //TC : O(nLogn)
    //SC : O(n)
    public int [] smallerNumbersThanCurrentApproach2(int[] nums){
        HashMap<Integer, Integer> dictionary = new HashMap<Integer,Integer>();
        int[] result = Arrays.copyOf(nums, nums.length);
        Arrays.sort(result);

        for (int i =0 ; i< result.length ; i++){
            if(!dictionary.containsKey(result[i])) dictionary.put(result[i], i);
        }
        
        for (int i =0; i< nums.length; i++){
            result[i] = dictionary.get(nums[i]);
        }
        return result;
    }

    //TC : O(N)
    //SC : O(N)
    public int [] smallerNumbersThanCurrentApproach3(int[] nums){

        int[] countOfNumber = new int[101];
        int[] result = new int[nums.length];

        for (int i=0 ; i< nums.length; i++){
            countOfNumber[nums[i]]+=1;
        }
        //System.out.println(Arrays.toString(countOfNumber));

  
        for (int i =1; i< countOfNumber.length; i++){
            countOfNumber[i]+=countOfNumber[i-1];
        }
        //System.out.println(Arrays.toString(countOfNumber));

        for (int i =0 ; i< nums.length ; i++){
            result[i]= (nums[i]>0) ? countOfNumber[nums[i]-1]: 0;
        }

        return result;
        
    }
}