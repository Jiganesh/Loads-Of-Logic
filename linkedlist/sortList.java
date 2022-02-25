package linkedlist;

import java.util.*;

public class sortList{
    public static void main(String[] args) {
        System.out.println("This is an Interactive Problem Please Test the Solution in LeetCode");
    }
}

class SolutionSL {

    // Submitted By @Jiganesh

    // TC: O(NLogN)
    // SC: O(N)

    // Approach:
    // 1. Store the Elements in a ArrayList
    // 2. Sort the ArrayList
    // 3. Add the Sorted ArrayList Elements in the LinkedList

    // Runtime: 10 ms, faster than 59.15% of Java online submissions for Sort List.
    // Memory Usage: 49.4 MB, less than 81.61% of Java online submissions for Sort List.

    public ListNode sortList(ListNode head) {
        
        List <Integer> storeLLinArrayList = new ArrayList<Integer>();
        
        ListNode curr = head;
        while (curr!= null){
            
            storeLLinArrayList.add(curr.val);
            curr = curr.next;
            
        }
        
        Collections.sort(storeLLinArrayList);
            
        curr = head;
        for (int i = 0 ; i< storeLLinArrayList.size(); i++){
            curr.val = storeLLinArrayList.get(i);
            curr = curr.next;
        }
        
        return head;  
    }


    // TC: O(NLogN)
    // SC: O(N)
    public ListNode sortListApproach2(ListNode head) {
        
        if(head==null || head.next ==null) return head;
        
        ListNode temp = head, slow = head, fast = head;
        
        // Find middle of the linkedlist with slow-fast pointer approach
        while (fast != null && fast.next != null){
            temp = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // Make two Parts of that LinkedList
        temp.next = null;
        
        ListNode first = sortListApproach2(head);
        ListNode second = sortListApproach2(slow);
        
        return merge(first , second);
        
    }
    
    public ListNode merge(ListNode pointer1, ListNode pointer2){
        
        ListNode Dummy = new ListNode(-1);
        ListNode pointerDummy = Dummy;
        
        while (pointer1 !=null && pointer2 != null){
            if (pointer1.val < pointer2.val){
                pointerDummy.next = pointer1;
                pointer1 = pointer1.next;
            }else{
                pointerDummy.next = pointer2;
                pointer2 = pointer2.next;
            }
            pointerDummy = pointerDummy.next;
        }
        
        if (pointer1 != null) pointerDummy.next = pointer1;
        if (pointer2 != null) pointerDummy.next = pointer2;
        
        return Dummy.next;   
    }
}