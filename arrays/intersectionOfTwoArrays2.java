class Solution {
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
}
