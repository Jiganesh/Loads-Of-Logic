package arrays;
import java.util.*;

// https://leetcode.com/problems/intersection-of-two-arrays-ii/


public class intersectionOfTwoArraysII{
    public static void main(String[] args) {

        SolutionIOTAII solution = new SolutionIOTAII ();
        System.out.println(Arrays.toString(solution.intersect(new int[]{1,2,2,1}, new int[]{2,2})));  
        System.out.println(Arrays.toString(solution.intersectApproach2(new int[]{1,2,2,1}, new int[]{2,2})));        

    }
}
class SolutionIOTAII {
    public int[] intersect(int[] nums1, int[] nums2) {
        
        HashMap<Integer, Integer> al = new HashMap<Integer, Integer>();
        
        int len1 = nums1.length;
        int len2 = nums2.length;
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int i=0;i<len1;i++){
            if(al.get(nums1[i]) == null)
                  al.put(nums1[i],1);
            else{
                int k = al.get(nums1[i]);
                al.put(nums1[i], k + 1);
            }
        }
        
        for(int i=0;i<len2;i++){
            if(al.get(nums2[i]) != null && al.get(nums2[i]) != 0){
                list.add(nums2[i]);
                int k = al.get(nums2[i]);
                al.put(nums2[i], k - 1);
            }
        }
        
        int res_len = list.size();
        int res[] = new int[res_len];
        for(int i=0;i<res_len;i++){
            res[i] = list.get(i);
        }
        
        return res;
      
    }

    public int[] intersectApproach2(int[] nums1, int[] nums2) {

        
        
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
