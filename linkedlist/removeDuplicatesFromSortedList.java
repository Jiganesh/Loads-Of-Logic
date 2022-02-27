// https://leetcode.com/problems/remove-duplicates-from-sorted-list/
package linkedlist;

public class removeDuplicatesFromSortedList {
    public static void main(String[] args) {

        System.out.println("This is an Interactive Problem, Please Test Solutions on Leetcode");
        
    }
}

class SolutionRDFSL {

    // TC : O(N)
    // SC : O(1)
    public ListNode deleteDuplicates(ListNode head) {
        
        ListNode current = head ;
        ListNode unique = current;
        
        while (current !=null){
            
            while (current != null && unique.val == current.val){
                current= current.next;
            }
            unique.next =current;
            unique = unique.next;
        }
        
        
        return head; 
    }

    // TC : O(N)
    // SC : O(1)

    // Better Appoach than previous one

    // Runtime: 0 ms, faster than 100.00% of Java online submissions for Remove Duplicates from Sorted List.
    // Memory Usage: 41.8 MB, less than 44.87% of Java online submissions for Remove Duplicates from Sorted List.
    
    public ListNode deleteDuplicatesApproach2(ListNode head) {
        
        ListNode current = head ;
        
        while(current != null && current.next != null){
            if (current.val == current.next.val){
                current.next = current.next.next;
            }else{
                current = current.next;
            }
        }
        return head;
    }
}