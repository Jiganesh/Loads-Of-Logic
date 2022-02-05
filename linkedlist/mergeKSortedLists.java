class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<Integer> al = new PriorityQueue<Integer>(); // Min-Heap 
        int len = lists.length;
        int k = 0;
        for(int i=0;i<len;i++){
            ListNode p = lists[i];
            while(p != null){
                al.add(p.val);
                p = p.next;
                k++;
            }
            
        }
        ListNode ff = new ListNode();
        if(k < 1){
             return null;
        }
        ListNode head = new ListNode(al.poll(),null);
        ListNode dumy = head;
        k = k  - 1;
        while( k > 0){
            int yy = al.poll();
            dumy.next = new ListNode(yy,null);
            dumy = dumy.next;
            k--;
        }
          
        return head;    
    }
}
