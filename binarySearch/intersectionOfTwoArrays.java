package binarySearch;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

public class intersectionOfTwoArrays {
    public static void main(String[] args) {
        SolutionIOTA solution = new SolutionIOTA();
        //System.out.println(Arrays.toString(solution.intersection(new int[]{1,2,2,1}, new int[]{2,2})));
        //System.out.println(Arrays.toString(solution.intersection(new int[]{4,9,5}, new int[]{9,4,9,8,4})));
        //System.out.println(Arrays.toString(solution.intersection(new int[]{1}, new int[]{1})));

        System.out.println(Arrays.toString(solution.intersectionHashSetSolution(new int[]{1,2,2,1}, new int[]{2,2})));
        System.out.println(Arrays.toString(solution.intersectionHashSetSolution(new int[]{4,9,5}, new int[]{9,4,9,8,4})));
        System.out.println(Arrays.toString(solution.intersectionHashSetSolution(new int[]{1}, new int[]{1})));

    }
}


class SolutionIOTA {
    // Approach 1 - Using Sorted Arrays and Hashset
    // TC = O(nLogn+mLogm)
    // SC = O(n+m)
    public int[] intersection(int[] nums1, int[] nums2) {

        ArrayList <Integer> list = new ArrayList<Integer>();

        Arrays.sort(nums1);
        Arrays.sort(nums2);

        for(int i = 0 ; i<=nums2.length-1; i++){
            int target = nums2[i] ;
            if( binarySearch(nums1, target, 0, nums1.length-1)){
                if (list.size()<=0 || target != list.get(list.size()-1)) list.add(target);
            }

        }
        int[] result = new int[list.size()];
        for (int j = 0 ; j<=list.size()-1; j++){
            result[j]=(list.get(j));
        }
        return result;
        
        
    }

    public boolean binarySearch (int [] array , int target ,int start , int end){

        if (start <= end ){
            int mid = start + (end -start)/2;
            if (array[mid]== target) return true;
            else if (array[mid]<target)  return binarySearch(array, target, mid+1, end);
            else return binarySearch(array, target, start, mid-1);
        }
        return false;
    }

    // Approach 2 - Using HashSet
    // TC = O (n+m)
    // SC = O (min(n,m))

    public int[] intersectionHashSetSolution(int[] nums1, int[] nums2) {
        HashSet<Integer> nums1HashSet= new HashSet<Integer>();
        HashSet<Integer> intersectionSet = new HashSet<Integer>();

        for (int i : nums1) nums1HashSet.add(i);
        for (int i : nums2){
            if(nums1HashSet.contains(i)) intersectionSet.add(i);
        }

        Object [] array = intersectionSet.toArray();
        int [] result = new int[array.length];
        for (int j = 0 ; j<intersectionSet.size(); j++){
            result[j]= (int)array[j];
        }
        return result;
    }
}