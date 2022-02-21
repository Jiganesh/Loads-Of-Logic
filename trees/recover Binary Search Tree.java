class Solution {
    ArrayList<Integer> al = new ArrayList<Integer>();
    HashMap<Integer, TreeNode> map = new HashMap<Integer, TreeNode>();
    public void Inorder(TreeNode r){
        
        if(r == null)
              return;
        Inorder(r.left);
        al.add(r.val);
        map.put(r.val, r);
        Inorder(r.right);
    }

    public void recoverTree(TreeNode root) {
        
        Inorder(root);
        int siz = al.size();
        int f[] = new int[siz];
        int p = 0;
        for(int i=0;i<siz;i++){
            f[i] = al.get(i);
        }
        Arrays.sort(f);
        int ff[] = new int[2];
        for(int i=0;i<siz;i++){
            if(f[i] != al.get(i)){
                TreeNode fst = map.get(f[i]);
                fst.val = al.get(i);
                 TreeNode snd = map.get(al.get(i));
                snd.val = f[i];
                break;
            }
        }
        al.clear();     
        
    
    }
}
