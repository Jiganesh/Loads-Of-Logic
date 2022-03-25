package trees;

public class balancedBinaryTree {
    public boolean isBalancedTree(TreeNode root) {
        return !(isBalTree(root) == -1);
    }

    private int isBalTree(TreeNode root) {
        if (root == null)
            return 0;
        int leftHeight = isBalTree(root.left);
        if (leftHeight == -1)
            return -1;
        int rightHeight = isBalTree(root.right);
        if (rightHeight == -1)
            return -1;
        if (Math.abs(leftHeight - rightHeight) > 1)
            return -1;
        else
            return Math.max(leftHeight, rightHeight) + 1;
    }
}
