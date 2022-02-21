//  https://leetcode.com/problems/recover-binary-search-tree/

package trees;

public class recoverBinarySearchTree {
    public static void main(String[] args) {
        System.out.println("This is an Interactive problem please Test the Solution In Leetcode");
    }
    
}


class SolutionRBST {

    // Submitted by @Jiganesh

    // Runtime: 4 ms, faster than 47.70% of Java online submissions for Recover Binary Search Tree.
    // Memory Usage: 47.2 MB, less than 19.94% of Java online submissions for Recover Binary Search Tree.
    
    // Efficient Approach
    
    // TC : O(N)
    // SC : O(1)
    private TreeNode first;
    private TreeNode last;
    private TreeNode prev;
    
    public void recoverTree(TreeNode root) {
        
        traverse(root);
        int temp = first.val;
        first.val= last.val;
        last.val = temp;
    }
    
    public void traverse (TreeNode root){
        
        if(root != null){
            traverse(root.left);
            
            if (first==null&& prev!= null && prev.val>root.val){ 
                first= prev;
                last = root;
            }else if (first!= null && prev!= null && prev.val>root.val){
                last = root;
            }
            
            prev = root;
            traverse(root.right);
        }
    }
}