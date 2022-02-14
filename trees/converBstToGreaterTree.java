class Solution {
    
    ArrayList<Integer> al = new ArrayList<Integer>();
    HashMap<Integer, TreeNode> map = new HashMap<Integer, TreeNode>();
    public void Inorder(TreeNode r){
        if(r == null)
            return;
        Inorder(r.left);
        al.add(r.val);
        map.put(r.val, r);
        Inorder(r.right);
        
    }
    
    public TreeNode convertBST(TreeNode root) {
        
        if(root == null || (root.left == null && root.right == null))
             return root;
        
      Inorder(root);
        int siz = al.size();
        int sum = 0;
        for(int i=0;i<siz;i++)
            sum += al.get(i);
        TreeNode tt = map.get(al.get(0));
        tt.val = sum;
 
        for(int i = 1; i<siz;i++){
            TreeNode dum = map.get(al.get(i));
            sum = sum - al.get(i - 1);
            dum.val = sum;
        }
     return root;
    }
   
}
