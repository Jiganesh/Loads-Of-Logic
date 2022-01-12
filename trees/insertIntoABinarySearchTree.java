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
        
        if (root ==null) return new TreeNode(val);
        
        TreeNode currentnode = root;
        while(currentnode !=null){
            if (currentnode.val < val) {
                if (currentnode.right != null){
                    currentnode = currentnode.right;
                    }else{
                    currentnode.right= new TreeNode(val);
                    break;
                    }
            }else{
                if( currentnode.left != null){
                    currentnode = currentnode.left;
                }else{
                    currentnode.left = new TreeNode(val);
                    break;
                }
                
            }
        }
        return root;
    }
}