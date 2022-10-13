// https://leetcode.com/problems/add-two-numbers/


// Runtime: 174 ms, faster than 52.10% of JavaScript online submissions for Add Two Numbers.
// Memory Usage: 48.7 MB, less than 12.42% of JavaScript online submissions for Add Two Numbers.


//  Definition for singly-linked list.
function ListNode(val, next) {
      this.val = (val===undefined ? 0 : val)
      this.next = (next===undefined ? null : next)
}
 
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */


var addTwoNumbers = function(l1, l2) {
    let sumNode = null;
    
    const carry = arguments[2];
    
    if (l1 || l2) {
        const val1 = l1 ? l1.val : 0;
        const val2 = l2 ? l2.val : 0;
        const next1 = l1 ? l1.next : null;
        const next2 = l2 ? l2.next : null;
        const val = carry ? val1 + val2 + 1 : val1 + val2;
        sumNode = new ListNode(val % 10);
        sumNode.next = addTwoNumbers(next1, next2, val >= 10);
    } else if (carry) {
        sumNode = new ListNode(1);
        sumNode.next = null;
    }
    return sumNode;
};