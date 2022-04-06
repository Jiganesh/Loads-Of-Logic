package linkedlist;

// https://leetcode.com/problems/plus-one-linked-list/

public class PlusOneLinkedList {
    public ListNode addToNum(ListNode head) {
        int sum = 0, carry = 1;
        ListNode newHead = reverse(head);
        ListNode currentNode = newHead, prevNode = newHead;
        while (currentNode != null) {
            sum = carry + currentNode.val;
            currentNode.val = sum % 10;
            carry = sum / 10;
            prevNode = currentNode;
            currentNode = currentNode.next;
        }
        if (carry > 0)
            prevNode.next = new ListNode(carry);
        head = reverse(newHead);
        return head;
    }

    private ListNode reverse(ListNode head) {
        if (head == null || head.next == null)
            return head;
        ListNode newHead = reverse(head.next);
        head.next.next = head;
        head.next = null;
        return newHead;
    }
}
