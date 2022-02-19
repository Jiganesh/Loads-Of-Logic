package trees;

class SolutionIIABST {

    public TreeNode insertIntoBST(TreeNode root, int val) {
        TreeNode newNode = new TreeNode(val);
        if (root== null) return newNode;

        TreeNode currentNode = root;
        while(currentNode!=null){

            if(currentNode.val> val){
                if (currentNode.left !=null){
                    currentNode = currentNode.left;
                }else{
                    currentNode.left= newNode;
                    break;
                }
            }else{
                if (currentNode.right !=null){
                    currentNode = currentNode.right;
                }else{
                    currentNode.right= newNode;
                    break;
                }
            }
        }
        return root;
    }

    // Efficient  (no nested conditions)
    public TreeNode insertIntoBSTApproach2(TreeNode root, int val) {

        // Making newNode for val
        // initializing root to currentNode to traverse
        TreeNode newNode = new TreeNode(val);
        TreeNode currentNode = root;

        //If root is null obviously we return newNode as it will be only node
        if (root == null) return newNode;

        
        while (true) {
            // we move if the val is greater to left or right if it is less and if the next node is not null
            if (currentNode.val > val && currentNode.left != null) {
                currentNode = currentNode.left;
                continue;
            }
            if (currentNode.val < val && currentNode.right != null) {
                currentNode = currentNode.right;
                continue;
            }

            // if next node is null based on the condition we insert to new node
            if (currentNode.val > val && currentNode.left == null) {
                currentNode.left = newNode;
                break;
            }
            if (currentNode.val < val && currentNode.right == null) {
                currentNode.right = newNode;
                break;
            }
        }
        return root;
    }
}
