class Solution {
ArrayList<Integer> al = new ArrayList<Integer>();
    public void Small(TreeNode r, int k, int i){
        
      if(r == null)
          return;

      Small(r.left, k , i);
        al.add(r.val);
      Small(r.right, k, i);  
    
    }
    
    
    public int kthSmallest(TreeNode root, int k) {
     
        Small(root, k, 0);
        return al.get(k - 1);
    
    }
}
