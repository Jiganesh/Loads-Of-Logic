// https://leetcode.com/problems/maximum-depth-of-binary-tree/

package trees;

public class maximumDepthOfBinaryTree {
    public static void main(String[] args) {
        System.out.println("This is an Interactive Problem please Test the solution on Github");
    }
}


class SolutionMDOBT{

    // Submitted by @rajput-hemant
    public int maxDepth(TreeNode root) {
    
    if (root == null)
        return 0;
    int depth = Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    return depth;

    }
}
