// https://leetcode.com/problems/majority-element/

package arrays;

import java.util.HashMap;

public class majorityElement {
    public static void main(String[] args) {

        SolutionME solution = new SolutionME();
        System.out.println(solution.majorityElement(new int[]{3,2,3}));
        System.out.println(solution.majorityElement(new int[]{2,2,1,1,1,2,2,}));

        
        System.out.println(solution.majorityElementApproach2(new int[]{3,2,3}));
        System.out.println(solution.majorityElementApproach2(new int[]{2,2,1,1,1,2,2,}));
        
    }
}


class SolutionME {

    // Submitted By @Jiganesh

    // TC : O(n)
    // SC : O(n)

    // BruteForce Approach

    public int majorityElement(int[] nums) {

        HashMap <Integer, Integer> dictionary =new HashMap <Integer, Integer>();
        
        for(int i : nums){
            dictionary.put(i, dictionary.getOrDefault(i,0)+1);
        }
        
        for (int i : dictionary.keySet()){
            if (dictionary.get(i)> nums.length/2) return i;
        }
        
        return 0;
    }


    // TC : O(n)
    // SC : O(1)

    // Efficient Approach

    public int majorityElementApproach2(int[] nums) {
        
        int count = 0;
        int majorityElement = nums[0];
        
        for (int i : nums){
            if (majorityElement==i) count++;
            else{
                count--;
                if(count==0) {
                    majorityElement = i;
                    count=1;
                }
            }
        }
        return majorityElement;   
    }
}