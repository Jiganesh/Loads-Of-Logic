class Solution {
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
