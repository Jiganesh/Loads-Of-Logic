package arrays;

import java.util.ArrayList;
import java.util.List;

// https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

public class allDivisionsWithTheHighestScoreOfABinaryArray{
    public static void main(String[] args) {
        SolutionADWTHSOABA solution = new SolutionADWTHSOABA();
        System.out.println(solution.maxScoreIndices(new int[]{0,0,1,0}));
        System.out.println(solution.maxScoreIndices(new int[]{0,0,0}));
        System.out.println(solution.maxScoreIndices(new int[]{1,1}));

    }
}


class SolutionADWTHSOABA {
    public List<Integer> maxScoreIndices(int[] nums) {

        int n = nums.length;
        List<Integer>  score = new ArrayList<Integer>();
        List <Integer> result  = new ArrayList<Integer>();
    

        int countOnes = 0;
        int countZeros = 0;

        // Counting All the ones and adding first initial score
        for(int i = 0 ; i<n ; i++) if(nums[i]==1) countOnes++;

        score.add(countOnes);


        for (int i = 0 ; i<n ; i++){
            if (nums[i]==0) countZeros++;
            else if (nums[i]==1) countOnes--;
            score.add(countOnes+countZeros);
        }

        int maximum = 0;
        
        for (int i =0 ; i<score.size(); i++){

            if (score.get(i)==maximum){
                result.add(i);
            }else if (score.get(i)>maximum){
                result.clear();
                result.add(i);
                maximum= score.get(i);
            }
        } 

        return result;
    }
}