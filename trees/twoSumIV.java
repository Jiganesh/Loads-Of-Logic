package trees;

import java.util.HashSet;

// https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

public class twoSumIV {
    public boolean findTarget(TreeNode root, int sum) {
        HashSet<Integer> set = new HashSet<>();
        return findTarget(root, sum, set);
    }

    private boolean findTarget(TreeNode root, int sum, HashSet<Integer> set) {
        if (root == null)
            return false;
        if (findTarget(root.left, sum, set) == true)
            return true;
        if (set.contains(sum - root.val))
            return true;
        else
            set.add(root.val);
        return findTarget(root.right, sum, set);
    }
}
