package arrays;

// https://leetcode.com/problems/merge-sorted-array/
// Solution : https://www.youtube.com/watch?v=C4oBXLr3zos


public class mergeSortedArray{
    public static void main(String[] args) {
        System.out.println( "Test Cases are Commented below , Please test it in leetcode" );

        /*
        [0]
        0
        [1]
        1
        [1]
        1
        []
        0
        [1,2,3,0,0,0]
        3
        [2,5,6]
        3
        */
        
    }
}
class SolutionMSA {

    // Submitted by @kushvr
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        
        if(n == 0)
            return ;
        if(m == 0){
            for(int i=0;i<n;i++)
                nums1[i] = nums2[i];
            
            return;
        }
        
        int ar[] = new int[m + n];
        int ar_p = 0;
        int i = 0;
        int j = 0;
        while(i != m && j != n){
            
            if(nums1[i] > nums2[j]){
                ar[ar_p] = nums2[j];
                j++;
                ar_p++;
            }else{
                ar[ar_p] = nums1[i];
                i++;
                ar_p++;
                
        }
        
        if(i == m && j != n){
            while(j != n){
                ar[ar_p] = nums2[j];
                j++;
                ar_p++;
            }
        }
        
        if(i != m && j == n){
            while(i != m){
                ar[ar_p] = nums1[i];
                i++;
                ar_p++;
            }
        }
    
        
        for(int in=0;in<(m + n);in++) nums1[in] = ar[in];  
      
        }
    }

    // Submitted by Jiganesh;

    // TC : O(N)
    // SC : O(1)


    // Runtime: 0 ms, faster than 100.00% of Java online submissions for Merge Sorted Array.
    // Memory Usage: 40.3 MB, less than 7.49% of Java online submissions for Merge Sorted Array.
    public void mergeApproach2(int[] nums1, int m, int[] nums2, int n) {
        
        int p1 = m -1;
        int p2 = n-1 ;
        int i = m+n-1;
        
        while (p2>= 0 ){
            if (p1>=0 && nums1[p1] > nums2[p2]){
                nums1[i--]=nums1[p1--];
            }else{
                nums1[i--]=nums2[p2--];
            }
        }
        
    }
}

