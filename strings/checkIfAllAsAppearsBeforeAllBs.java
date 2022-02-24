// https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

package strings;

public class checkIfAllAsAppearsBeforeAllBs {
    public static void main(String[] args) {

        SolutionCIAAABAB solution = new SolutionCIAAABAB();

        System.out.println(solution.checkString("aab"));
        System.out.println(solution.checkString("abab"));
        System.out.println(solution.checkString("bbb"));

    }   
}


class SolutionCIAAABAB {

    // Submitted By @Jiganesh

    // TC: O(N)
    // SC: O(1)

    // Runtime: 1 ms, faster than 76.44% of Java online submissions for Check if All A's Appears Before All B's.
    // Memory Usage: 42.6 MB, less than 5.52% of Java online submissions for Check if All A's Appears Before All B's
    
    public boolean checkString(String s) {
        boolean occuredb = false;
        
        for (int i = 0; i<s.length(); i++){

            // check if any b has occured in string
            if (occuredb == false && s.charAt(i)=='b') occuredb = true;

            // check if b has occured and a has occured after it
            if (occuredb && s.charAt(i)=='a') return false;
        }
        return true;
    }
}

