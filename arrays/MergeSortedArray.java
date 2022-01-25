class Solution {
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
        
        
        for(int in=0;in<(m + n);in++)
             nums1[in] = ar[in];  
        
    }
}
