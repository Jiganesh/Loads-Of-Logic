package trees;

import java.util.LinkedList;
import java.util.List;

// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

import java.util.Stack;

public class binaryTreeZigzagLevelOrderTraversal {
    public static List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new LinkedList<>();
        if (root == null)
            return result;
        Stack<TreeNode> stk1 = new Stack<>(), stk2 = new Stack<>();
        stk1.push(root);
        while (!stk1.isEmpty() || !stk2.isEmpty()) {
            List<Integer> list1 = new LinkedList<>();
            while (!stk1.isEmpty()) {
                TreeNode currentTreeNode = stk1.pop();
                list1.add(currentTreeNode.val);
                if (currentTreeNode.left != null)
                    stk2.push(currentTreeNode.left);
                if (currentTreeNode.right != null)
                    stk2.push(currentTreeNode.right);
            }
            if (!list1.isEmpty())
                result.add(list1);
            List<Integer> list2 = new LinkedList<>();
            while (!stk2.isEmpty()) {
                TreeNode currentTreeNode = stk2.pop();
                list2.add(currentTreeNode.val);
                if (currentTreeNode.right != null)
                    stk1.push(currentTreeNode.right);
                if (currentTreeNode.left != null)
                    stk1.push(currentTreeNode.left);
            }
            if (!list2.isEmpty())
                result.add(list2);
        }
        return result;
    }
}
