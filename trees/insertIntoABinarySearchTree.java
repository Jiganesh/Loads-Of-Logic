package trees;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        
       TreeNode NewNode = new TreeNode(val);
         TreeNode dummy = root;
        
        if(root == null)
            return NewNode;
            
        
         while(true)
         {
             if(dummy.val > val && dummy.left == null){
                   dummy.left = NewNode;
                 break;
             }
             if(dummy.val < val && dummy.right == null){
                   dummy.right = NewNode;
                 break;
             }
             
             if(dummy.val > val && dummy.left != null){
                  dummy = dummy.left;
                 continue;
             }
             if(dummy.val < val && dummy.right != null){
                 dummy = dummy.right;
                 continue;
             }    
         }
        
        
        return root;
 }}
