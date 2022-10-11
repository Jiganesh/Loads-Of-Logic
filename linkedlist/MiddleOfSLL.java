package LinkedList.singlyLinkedList;

public class MiddleOfSLL {

    static Node head;

    static class Node{
        private int data;
        private Node next;

        public Node(int data){
            this.data = data;
            this.next = null;
        }
    }

    void print(Node head){
        while(head != null){
            System.out.print(head.data + " -> ");
            head = head.next;
        }
        System.out.println("Null");
    }

    int findMid(Node node){
        Node fastPtr = node;
        Node slowPtr = node;

        while(fastPtr != null && fastPtr.next != null){
            fastPtr = fastPtr.next.next;
            slowPtr = slowPtr.next;
        }
        return slowPtr.data;
    }

    public static void main(String[] args) {
        MiddleOfSLL mid = new MiddleOfSLL();
        mid.head = new Node(1);
        mid.head.next = new Node(2);
        mid.head.next.next = new Node(3);
        mid.head.next.next.next = new Node(4);
        mid.head.next.next.next.next = new Node(5);

        mid.print(head);
        System.out.println(mid.findMid(head));

    }
}
