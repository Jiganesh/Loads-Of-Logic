package stack;

import java.util.Stack;

// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

public class removeAllAdjacentDuplicatesInString {
    public static String removeDuplicates(String s) {
        Stack<Character> stk = new Stack<>();
        for (char ch : s.toCharArray()) {
            if (!stk.isEmpty() && ch == stk.peek())
                stk.pop();
            else
                stk.push(ch);
        }
        StringBuilder sb = new StringBuilder();
        for (char ch : stk)
            sb.append(ch);
        return sb.toString();
    }
}
