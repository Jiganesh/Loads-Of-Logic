// https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

package dynamicProgramming;
/*
 * Minimum Insertion Steps to Make a String Palindrome
    Q: Can you please explain more how exactly lcs with its reverse helps?
    A: An example could be illustrative. e.g., "mbadm". Let's mark the characters not in LCS:
    "mbadm"
    Reverse:
    "mdabm"
    We need at least 2 insertions - b and d - to make them palindromes:
    "mbdadbm" or
    "mdbabdm"

    More similar LCS problems:
1092. Shortest Common Supersequence and Solution
1062. Longest Repeating Substring (Premium).
516. Longest Palindromic Subsequence
1312. Minimum Insertion Steps to Make a String Palindrome

Find the size of the longest common subsequence between the original string and its reverse, deduct it from the size of the original string, that is the solution.

Analysis:
Time & space: O(n ^ 2), where n = s.length().
 */


public class minimumInsertionStepstoMakeaStringPalindrome {
    public static void main(String[] args) {
        String in1 = "zzazz"; // expected 0
        String in2 = "mbadm"; // 2
        String in3 = "leetcode"; // 5

        System.out.println(minInsertions(in1));
        System.out.println(minInsertions(in2));
        System.out.println(minInsertions(in3));

    }
    
    public static int minInsertions(String s) {
        String r = new StringBuilder(s).reverse().toString();
        return s.length() - lcs(s, r);
    }

    public static int lcs(String s, String r) {
        int n = s.length();
        int[][] dp = new int[n + 1][n + 1];
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                dp[i + 1][j + 1] = s.charAt(i) == r.charAt(j) ? dp[i][j] + 1 : Math.max(dp[i + 1][j], dp[i][j + 1]);
        return dp[n][n];
    }
    
}

