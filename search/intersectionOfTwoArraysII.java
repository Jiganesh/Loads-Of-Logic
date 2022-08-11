package search;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Arrays;

public class intersectionOfTwoArraysII {
    public static void main(String[] args) {
        SolutionIOTAII solution = new SolutionIOTAII();
        System.out.println(Arrays.toString(solution.intersect(new int[]{1,2,2,1}, new int[]{2,2})));
        System.out.println(Arrays.toString(solution.intersect(new int[]{4,9,5}, new int[]{9,4,9,8,4})));
        System.out.println(Arrays.toString(solution.intersect(new int[]{1}, new int[]{1})));

    }
}

class SolutionIOTAII {
    public int[] intersect(int[] nums1, int[] nums2) {

        // TimeComplexity = O(n+m)
        // SpaceComplexity = O(min(n,m))

        HashMap<Integer,Integer> dictionary = new HashMap<Integer, Integer>();
        List<Integer> list = new ArrayList<Integer>();
        for(int i:nums1){
            if(dictionary.containsKey(i)) dictionary.put(i, dictionary.get(i)+1);
            else dictionary.put(i, 1);
        }
        for (int j : nums2){
            if (dictionary.containsKey(j) && dictionary.get(j)>0){
                dictionary.put(j, dictionary.get(j)-1);
                list.add(j) ;
            }
        } 
        
        int [] result = new int[list.size()];
        for(int i=0; i<list.size(); i++){
            result[i]=list.get(i);
        }
        return result;
    }
}
