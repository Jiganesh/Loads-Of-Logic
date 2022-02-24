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
}