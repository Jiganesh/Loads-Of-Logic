// https://leetcode.com/problems/remove-k-digits/

package stack;

import java.util.Stack;

public class removeKDigits {
    public static void main(String[] args) {
        SolutionRKD solution = new SolutionRKD();
        System.out.println(solution.removeKdigits("1432219", 3));
    }

}

class SolutionRKD {
    public String removeKdigits(String num, int k) {

        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < num.length(); i++) {
            char number = num.charAt(i);

            while (!stack.isEmpty() && k > 0 && stack.peek() - '0' > (number - '0')) {
                stack.pop();
                k--;
            }

            if (!stack.isEmpty() || number != '0')
                stack.push(number);

        }

        while (k > 0 && !stack.isEmpty()) {
            stack.pop();
            k--;
        }

        if (stack.size() == 0)
            return "0";

        StringBuilder sb = new StringBuilder();
        for (char i : stack) {
            sb.append(i);
        }

        return new String(sb);
    }
}
