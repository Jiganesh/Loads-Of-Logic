package trees;

// https://leetcode.com/problems/binary-tree-right-side-view/

import java.util.ArrayList;
import java.util.List;

public class binaryTreeRightSideView {
    int maxLevel = 0;
    List<Integer> arr = new ArrayList<Integer>();

    public List<Integer> rightSideView(TreeNode root) {
        rightSideView(root, 1);
        return arr;
    }

    private void rightSideView(TreeNode root, int level) {
        if (root == null)
            return;
        if (maxLevel < level) {
            arr.add(root.val);
            maxLevel = level;
        }
        rightSideView(root.right, level + 1);
        rightSideView(root.left, level + 1);
    }
}
