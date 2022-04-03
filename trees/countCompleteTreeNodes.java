package trees;

// https://leetcode.com/problems/count-complete-tree-nodes/

public class countCompleteTreeNodes {

    // Approach 1
    // Time Complexity -> O(n)
    public int countNodes(TreeNode root) {
        if (root == null)
            return 0;
        return countNodes(root.left) + countNodes(root.right) + 1;
    }

    // Approach 2
    // Time Complexity -> O(logn * logn)
    public int countNodes2(TreeNode root) {
        int leftHeight = 0, rightHeight = 0;
        TreeNode currentNode = root;
        while (currentNode != null) {
            leftHeight++;
            currentNode = currentNode.left;
        }
        currentNode = root;
        while (currentNode != null) {
            rightHeight++;
            currentNode = currentNode.right;
        }
        if (leftHeight == rightHeight)
            return (int) Math.pow(2, leftHeight) - 1;
        return countNodes2(root.left) + countNodes2(root.right) + 1;
    }
}
