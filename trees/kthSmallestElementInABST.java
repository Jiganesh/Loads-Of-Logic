// https://leetcode.com/problems/kth-smallest-element-in-a-bst/

package trees;

public class kthSmallestElementInABST {
	public static void main(String[] args) {

		System.out.println("This is an Interactive problem please Test the Solution In Leetcode");

	}
}

class SolutionKSEIABST {

	// Submitted by @Jiganesh
	// TC : O(N)
	// SC : O(1)
	public int kthSmallest(TreeNode root, int k) {

		int[] array = new int[2];
		array[0] = k;
		traverse(array, root);
		return array[1];
	}

	public int[] traverse(int[] array, TreeNode root) {
		if (root != null) {
			traverse(array, root.left);
			if (--array[0] == 0)
				array[1] = root.val;
			traverse(array, root.right);
		}
		return array;
	}
}