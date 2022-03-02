// https://leetcode.com/problems/is-subsequence/

package stack;

import java.util.*;

public class isSubsequence {

    public static void main(String[] args) {

        SolutionIS solution = new SolutionIS();
        System.out.println(solution.isSubsequence("abc","ahbgdc"));
        System.out.println(solution.isSubsequence("", "aa"));

        System.out.println(solution.isSubsequenceApproach2("b", "abc"));
        System.out.println(solution.isSubsequenceApproach2("axc", "ahbgdc"));
        System.out.println(solution.isSubsequenceApproach2("", "ahbgdc")); //true

        
    }
    
}

class SolutionIS {


    // Submitted by Jiganesh

    // TC : O(N+M)
    // SC : O(N)


    // Runtime: 2 ms, faster than 45.06% of Java online submissions for Is Subsequence.
    // Memory Usage: 40.2 MB, less than 52.80% of Java online submissions for Is Subsequence.
    public boolean isSubsequence(String s, String t) {
        
        Stack<Character> stack = new Stack<Character>();
        
        for (int i =0; i<s.length(); i++){
            stack.push(s.charAt(i));
        }
        
        for (int i = t.length()-1; i>=0 ; i--){
            if (!stack.empty() && stack.peek()==t.charAt(i)) stack.pop();
        }
        
        return stack.empty();
        
    }

    // TC: O(N+M)
    // SC : O(1)

    // Runtime: 0 ms, faster than 100.00% of Java online submissions for Is Subsequence.   
    // Memory Usage: 40.2 MB, less than 52.80% of Java online submissions for Is Subsequence.
    public boolean isSubsequenceApproach2(String s, String t) {

        
        int pointerOnS = s.length()-1;
        int pointerOnT = t.length()-1;


        while(pointerOnT >= 0 && pointerOnS>=0){

            while(pointerOnT>=0 && t.charAt(pointerOnT) != s.charAt(pointerOnS)){
                pointerOnT--;
            }

            if (pointerOnS>=0&&pointerOnT>=0 && t.charAt(pointerOnT) == s.charAt(pointerOnS)){
                pointerOnS--;
                pointerOnT--;
            }
            
        }

        return pointerOnS<0;
    }


    // Modified Above Approach Same Complexities but aesthetic
    public boolean isSubsequenceApproach3(String s, String t) {

        int pointerOnS = s.length()-1;
        int pointerOnT = t.length()-1;


        while(pointerOnT >= 0 && pointerOnS>=0){

            if(t.charAt(pointerOnT) != s.charAt(pointerOnS)){
                pointerOnT--;
            }else{
                pointerOnS--;
                pointerOnT--;
            }
            
        }

        return pointerOnS<0;
    }
}
