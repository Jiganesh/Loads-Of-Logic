package trees;


import java.util.*;

public class allElementsInTwoBinarySearchTrees{
    public static void main(String[] args) {
        System.out.println("Best to Check the Solution In Leetcode Itself as Binary Tree is not Implemented here");
    }
}

class Solution {
    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        List<Integer> result = new ArrayList<Integer>();
        
        traverse(result , root1);
        traverse(result , root2);
        
        Collections.sort(result);
        return result;
    }
    
    public void traverse(List<Integer> result , TreeNode root){
        if (root != null){
            traverse(result, root.left);
            result.add(root.val);
            traverse(result, root.right);
        }
    }
}