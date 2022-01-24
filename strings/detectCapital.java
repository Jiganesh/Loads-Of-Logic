package strings;

public class detectCapital {
    public static void main(String[] args) {

        SolutionDC solution = new SolutionDC();
        System.out.println(solution.detectCapitalUse("USA"));
        System.out.println(solution.detectCapitalUse("FLaG"));
        System.out.println(solution.detectCapitalUse("Google"));
        System.out.println(solution.detectCapitalUse("leetcode"));

        System.out.println();

        System.out.println(solution.detectCapitalUseApproach2("USA"));
        System.out.println(solution.detectCapitalUseApproach2("FLaG"));
        System.out.println(solution.detectCapitalUseApproach2("Google"));
        System.out.println(solution.detectCapitalUseApproach2("leetcode"));

    }
}


class SolutionDC {

    // TC : O(N)
    // SC : O(N)

    // Brute Force : Using Extra space
    public boolean detectCapitalUse(String word) {
        
        String allCapital = word.toUpperCase();
        String firstCapital = word.substring(0,1).toUpperCase()+word.substring(1).toLowerCase();
        String lowerCase = word.toLowerCase();

        return (word.equals(allCapital) || word.equals(firstCapital) || word.equals(lowerCase));
    }

    // TC : O(N)
    // SC : O(1)

    // Runtime: 1 ms, faster than 99.35% of Java online submissions for Detect Capital.
    // Memory Usage: 39 MB, less than 43.48% of Java online submissions for Detect Capital.

    // Efficient Solution

    // o solve this problem, we count the number of capital letters in the word and then check all three conditions:

    // Number of capital letters is equal to the length of the word
    // Number of capital letters is zero
    // There is just one capital letter and it's the first letter

    // Time: O(n) - for the scan
    // Space: O(1)


    // Submitted by @ Kushvr
    public boolean detectCapitalUseApproach2(String word) {
        
        int len = word.length();
        int countOfCapitalLetters = 0;
        
        boolean firstLetterIsCapital = word.charAt(0) >=65 &&  word.charAt(0) <=90;

        for(int i=0;i<len;i++){
            int k = word.charAt(i);
            if(k>= 65 && k<= 90) countOfCapitalLetters++; 
        }
        return (
            countOfCapitalLetters == len || 
            (firstLetterIsCapital && countOfCapitalLetters==1)|| 
            countOfCapitalLetters==0
        ); 
    }
    
}