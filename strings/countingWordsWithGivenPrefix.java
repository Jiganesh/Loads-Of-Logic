package strings;

public class countingWordsWithGivenPrefix {
    public static void main(String[] args) {

        SolutionCWWGP solution = new SolutionCWWGP();
        System.out.println(solution.prefixCount(new String[]{"leetcode","win","loops","success"}, "code"));
        System.out.println(solution.prefixCount(new String[]{"pay","attention","practice","attend"}, "at"));

    }
}

class SolutionCWWGP {

    // Submitted by Jiganesh 

    // TC : O(N * M)
    // SC : O(N)

    // Runtime: 1 ms, faster than 83.33% of Java online submissions for Counting Words With a Given Prefix.
    // Memory Usage: 43.7 MB, less than 50.00% of Java online submissions for Counting Words With a Given Prefix.
    
    public int prefixCount(String[] words, String pref) {
        
        int count = 0;
        
        int lengthOfPref = pref.length();
        
        for (String word: words){

            // check if length of prefix is less or equal to word else there is not point in checking
            // extract the substring pref from word and check if it is equal to pref
            if (lengthOfPref<= word.length() && word.substring(0, lengthOfPref).equals(pref)){
                count++;
            }
        }
        return count;  
    }
}