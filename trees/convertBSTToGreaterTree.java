// https://leetcode.com/problems/convert-bst-to-greater-tree/
package trees;

public class convertBSTToGreaterTree{
    public static void main(String[] args) {
        System.out.println("This is an Interactive problem please Test the Solution In Leetcode");
    
    }
}

class SolutionCBSTTGT {


    // Submitted by @Jiganesh


    // Runtime: 0 ms, faster than 100.00% of Java online submissions for Convert BST to Greater Tree.
    // Memory Usage: 42.6 MB, less than 72.73% of Java online submissions for Convert BST to Greater Tree.
    

    // TC: O(N)
    // SC: O(1)
    private int[] array = new int[1];
    
    public TreeNode convertBST(TreeNode root) {
        
        traverse(root);
        return root;
        
    }
    
    public void traverse(TreeNode root){
    if (root != null ){
        traverse(root.right);
        array[0]+=root.val;
        root.val= array[0];
        traverse(root.left);
        }
    }
}