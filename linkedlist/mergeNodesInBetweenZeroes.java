package linkedlist;

public class mergeNodesInBetweenZeroes{
    public static void main(String[] args) {
        System.out.println("Interactive Problem So Test The Solution in Leetcode Itself");
    }
}


class SolutionMNIBZ {

    // Submitted by @Jiganesh
    
    // TC : O(n)
    // SC : O(1)

    public ListNode mergeNodes(ListNode head) {
        
        
        ListNode current = head;
        int summation = 0;
        
        while(current != null){
            if (current.val ==0){
                current.val =summation;
                summation=0;
            }else{
                summation+=current.val;
                current.val=0;
            }
            current= current.next;
        }
        
        current = head;
        while (current != null && current.next !=null){
            if (current.next.val==0  && current.next.next !=null){
                current.next = current.next.next;
            }else{
                current= current.next;
            }
        }
        return head.next;
    }
}