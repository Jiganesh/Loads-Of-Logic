package arrays;

import java.util.PriorityQueue;

public class medianOfTwoSortedArrays{
    public static void main(String[] args) {
        SolutionMOTSA solution = new SolutionMOTSA();
        int[] nums1 = {1, 3};
        int[] nums2 = {2};
        System.out.println(solution.findMedianSortedArrays(nums1, nums2));
    }
}
class SolutionMOTSA {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        
        int len1 = nums1.length;
        int len2 = nums2.length;
        
        PriorityQueue<Integer> al = new PriorityQueue<Integer>(); // Min-Heap
        for(int i=0;i<len1;i++)
            al.add(nums1[i]);
        for(int i=0;i<len2;i++)
            al.add(nums2[i]);
        
            int mid = (len1+len2)/2;
            int prev= 0;
            int curr = 0;
        if((len1+len2)%2 == 0)
        {
            int stp = 1;
            while(stp < (mid)){
                al.poll();
                stp += 1;
            }
            
            prev = al.poll();
            curr = al.poll();

            return (double)((prev+curr)/2.0);
        }else{
            
          
            int stp  = 0;
            while(stp < (mid + 1)){
                curr = al.poll();
                stp++;
            }
            return (double)curr;
        }
        
    }
}
