package arrays;

// https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class findAllLonelyNumbersInTheArray {
    public static void main(String[] args) {

        SolutionFALNITA solution = new SolutionFALNITA();
        System.out.println(solution.findLonely(new int[]{10,6,5,8}));
        System.out.println(solution.findLonely(new int[]{ 1,3,5,3}));
        
    }  
}


class SolutionFALNITA {

    // Submitted by @Jiganesh
    // TC: O(N)
    // SC: O(N)
    public List<Integer> findLonely(int[] nums) {
        
        HashMap <Integer, Integer> dictionary = new HashMap<Integer, Integer>();
        List <Integer> result = new ArrayList<Integer>();

        for (int i : nums) 
            dictionary.put(i, dictionary.getOrDefault(i, 0)+1);

        for (int i: nums){
            if(!dictionary.containsKey(i-1) &&  !dictionary.containsKey(i+1) && dictionary.get(i)==1){
                result.add(i);
            }
        }

        return result;
        


    }
}