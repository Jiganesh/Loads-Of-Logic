// https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

package strings;

import java.util.HashMap;

public class longestPalindromeByConcatenatingTwoLetterWords {
    public static void main(String[] args) {
        SolutionLPBCTLW solution = new SolutionLPBCTLW();
        System.out.println(solution.longestPalindrome(new String[]{"ab","ty","yt","lc","cl","ab"}));
        System.out.println(solution.longestPalindrome(new String[]{"kk","hh","gg","pp","kk","uu","ss","ii","ww","ee","qq","ff","ff","xx","ww","nn","tt","ff","oo","dd","bb","mm","qq","kk","ww","yy","qq","ww","zz","xx","ss","vv","bb","ee","qq","dd","rr","zz","fn","ww","ww","hh","qq","hh","rn","ww","ll","zz","nn","jj","jj","aa","hh","gg","xx","ll","tt","aa","xx","gg","ff","uu","fn","qq","ee","qq","hh","cc","xx","jj","dd","yy","tt","yy","yy","kk","fn","vv","ee","rr","rr","tt","ee","rr","kk","fn","tt","ll","vv","zz","xx","ee","hh","xx","gg","uu","ww","ww","yy","ss","zz","vv","jj","jj","aa","pp","ss","xx","ee","pp","xx","ss","rf","kk","vv","tt","nf","vv","oo","yy","jj","qq","fr","ww","kk","tt","kk","mm","aa","yy","ii","ii","ww","dd","qq","rf","uu","xx","ff","ee","nn","uu","ww","ww","pp","pp","aa","bb","kk","gg","vv","fr","vv","ll","xx","oo","kk","zz","yy","nn","oo","cc","vv","aa","bb","cc","ff","hh","xx","rf","qq","ll","uu","pp","ff","jj","oo","kk","fr","zz","ff","qq","mm","ee","uu","vv","oo","rr","pp","gg","yy","mm","rf","nr","zz","mm","xx","ss","ee","mm","nr","mm","qq","ii","jj","dd","nn","vv","ll","cc","qq","ii","aa","gg","hh","ss","ee","vv","ff","pp","qq","ff","nf","oo","ll","hh","aa","nf","gg","jj","hh","ff","kk","vv","oo","xx","rr","ee","ff","jj","pp","vv","nr","fn","qq","ee","mm","ww","ii","yy","ee","yy","gg","ll","dd","uu","hh","ii","ee","jj","pp","uu","tt","tt","ee","yy","jj","tt","rr","pp","ss","nn","fr","zz","oo","jj","mm","cc","ff","rr","rr","qq","zz","pp","qq","hh","uu","yy","dd","mm","ii","kk","ss","vv","jj","xx","jj","tt","jj","jj","yy","ww","zz","vv","vv","nn","aa","vv","kk","gg","zz","oo","nn","rf","zz","jj","jj","dd","uu","qq","pp","nn","rf","qq","aa","yy","ee","ss","bb","oo","oo","aa","ii","pp","ss","rr","jj","ii","ll","kk","cc","xx","uu","ii","vv","mm","gg","tt","ll","cc","yy","ee","xx","ww","tt","xx","bb","fn","ww","oo","jj","aa","cc","nr","hh","nn","nf","vv","ss","gg","cc","fn","kk","xx","ss","qq","rr","cc","zz","cc","ff","nf","tt","jj","kk","qq","vv","nn","xx","ww","aa","tt","rr","dd","oo","tt","uu","zz","cc","tt","aa","aa","aa","oo","ff","gg","gg","yy","ii","ee","nn","gg","yy","mm","rn","ii","gg","dd","cc","gg","gg","ss","hh","tt","jj","ff","aa","vv","oo","qq","nr","cc","hh","zz","dd","jj","ss","fn","mm","pp","rr","yy","gg","uu","ww","mm","kk","jj","pp","ss","nn","hh","tt","vv","jj","gg","fr","nn","ss","ii","ii","yy","bb","ww","jj","zz","ff","mm","jj","uu","ww","ss","pp","vv","jj","ss","rf","dd","fn","hh","tt","dd","fr","rf","dd","uu","cc","tt","dd","bb","vv","ee","cc","yy","fn","kk","nf","kk","aa","uu","dd","nn","ll","jj","ee","qq","oo","gg","vv","rr","ff","aa","ss","ee","ll","aa","ee","kk","ee","nf","yy","hh","mm","ss","qq","ww","bb","ff","fr","uu","zz","gg","cc","pp","yy","hh","ff","vv","qq","gg","uu","ff","mm","dd","aa","jj","tt","ee","ff","rf","hh","kk","qq","vv","pp","mm","gg","ff","jj","ll","fn","ff","ww","uu","oo","cc","cc","rr","zz","ww","ll","ii","ll","uu","dd","dd","ww","uu","fn","oo","mm","dd","ww","ee","vv","pp","pp","gg","hh","uu","qq","yy","oo","pp","ww","ll","ss","nn","ii","ff","ww","mm","kk","rf","cc","rr","ee","fr","gg","aa","ll","tt","vv","ll","kk","qq","ww","zz","ff","mm","ww","tt","dd","cc","ii","hh","ee","gg","ss","mm","cc","bb","oo","kk","zz","vv","ii","qq","nn","tt","kk","tt","ee","jj","ii","hh","ff","rr","pp","yy","cc","uu","rr","uu","ee","tt","ll","uu","gg","ee","ii","oo","ss","fr","ee","ii","ll","nr","hh","mm","jj","aa","dd","gg","rr","xx","cc","ee","nn","ss","hh","ff","ww","ww","cc","mm","zz","ll","fr","nn","ww","pp","fn","uu","ii","qq","ww","jj","hh","gg","yy","oo","hh","ii","qq","tt","uu","zz","zz","xx","kk","jj","ee","rr","ff","xx","nn","pp","yy","uu","hh","ll","uu","cc","gg","yy","oo","tt","zz","hh","ll","kk","gg","vv","rr","yy","ff","bb","hh","gg","aa","mm","zz","rr","mm","ii","pp","zz","nn","ii","uu","oo","jj","nf","dd","bb","ll","tt","ff","pp","jj","xx","zz","nn","cc","ww","vv","ff","uu","yy","nn","ff","cc","jj","oo","xx","nf","kk","cc","jj","gg","dd","vv","yy","vv","gg","gg","gg","cc","ee","tt","nn","ww","kk","fn","hh","yy","gg","ee","gg","jj","gg","bb","uu","qq","gg","ii","jj","gg","bb","rr","rf","tt","ff","tt","uu","hh","gg","kk","nr","fn","tt","zz","yy","yy","kk","dd","hh","dd","gg","yy","kk","uu","cc","ww","rn","ff","qq","ll","zz","vv","ff","cc","ff","ll","ss","ww","zz","vv","oo","bb","ii","ww","qq","kk","yy","ww","mm","gg","ss","qq","dd","oo","aa","nn","ww","rr","oo","pp","mm","ww","ww","ii","tt","qq","ss","zz","ee","qq","zz","cc","qq","aa","kk","rn","mm","hh","qq","qq","dd","ff","bb","pp","bb","zz","cc","uu","tt","ee","yy","qq","nn","aa","pp","oo","ss","dd","tt","ww","fr","ss","xx","fn","ee","ii","rr","zz","vv","dd","bb","cc","bb","cc","mm","jj","bb","tt","gg","kk","ii","xx","vv","vv","hh","ee","xx","ff","oo","oo","ee","yy","rr","oo","oo","ee","hh","oo","bb","nn","ii","kk","jj","uu","kk","gg","ii","ww","nr","gg","ss","rr","pp","tt","gg","ii","mm","zz","pp","tt","rf","ee","rr","ww","ee","xx","ee","nn","zz","ee","jj","nn","dd","jj","ss","aa","jj","hh","xx","nf","aa","tt","ee","kk","qq","qq","oo","gg","ll","aa","ll","nn","ii","gg","ii","vv","ll","rr","qq","ss","oo","dd","uu","ee","pp","ww","gg","oo","dd","qq","dd","pp","nf","ff","nr","ee","ee","jj","zz","qq","vv","oo","nr","ll","kk","rr","nn","gg","xx","yy","aa","vv","zz","nn","ii","ww","kk","jj","mm","qq","ss","cc","zz","kk","cc","gg","yy","dd","jj","nn","gg","tt","ff","gg","dd","ll","vv","bb","tt","oo","ii","rr","oo","mm","zz","oo","bb","ii","jj","yy","dd","mm","zz","ff","ww","rf","ww","ll","bb","bb","bb","ww","qq","ww","ff","ss","rr","ee","aa","gg","ff","ee","nn","mm","vv","cc","jj","fn","cc","ii","gg","qq","nn","vv","nn","jj","fr","zz","ss","hh","ee","rn","hh","kk","aa","dd","yy","uu","bb","hh","ee","pp","tt","rr","ss","zz","mm","rr","xx","oo","uu","tt","cc","qq","ss","tt","uu","ww","kk","mm","kk","qq","qq","ee","pp","ff","tt","oo","tt","ee","xx","cc","yy","fn","zz","fn","uu","bb","cc","ee","rf","bb","aa","yy","tt","xx","rr","jj","mm","aa","rr","pp","xx","rr","aa","mm","oo","cc","bb","ee","mm","mm","qq","ee","kk","zz","bb","vv","ee","hh","xx","uu","ss","qq","ll","hh","xx","uu","ll","aa","qq","ww","oo","tt","tt","ll","nn","bb","aa","ll","gg","vv","mm","dd","kk","cc","hh","ll","kk","uu","ww","bb","gg","tt","nn","zz","hh","rf","ll","kk","vv","xx","cc","oo","gg","bb","dd","dd","cc","zz","zz","ss","ss","aa","gg","pp","ii","hh","uu","qq","uu","uu","yy","vv","uu","ii","aa","mm","jj","nn","ss","ww","oo","qq","hh","aa","hh","ii","mm","ee","hh","cc","bb","rf","ww","tt","xx","pp","jj","tt","dd","kk","fn","ee","ww","pp","tt","hh","ll","kk","yy","dd","zz","uu","kk","yy","nn","ee","vv","gg","fn","aa","nr","ee","ee","bb","rr","kk","nn","tt","rr","oo","ll","mm","vv","zz","ss","hh","ee","ii","ff","bb","oo","tt","uu","jj","dd","cc","qq","rr","tt","gg","nn","ii","nn","uu","dd","ff","cc","vv","vv","hh","oo","pp","yy","ee","ee","pp","pp","dd","nf","hh","jj","uu","bb","jj","ff","xx","hh","rr","zz","kk","dd","yy","tt","yy","mm","ww","hh","cc","nf","zz","hh","ee","tt","vv","ww","ww","ll","pp","kk","uu","ee","oo","xx","rf","ww","kk","cc","vv","rr","dd","ss","dd","rr","yy","cc","zz","kk","ww","kk","dd","zz","jj","pp","hh","vv","yy","bb","oo","bb","aa","cc","mm","ss","mm","aa","qq","kk","hh","mm","rr","qq","gg","dd","gg","hh","oo","gg","ff","uu","ww","bb","dd","dd","qq","cc","yy","rf","oo","kk","tt","oo","ss","pp","oo","hh","gg","fn","nn","nn","rr","mm","tt","gg","cc","jj","yy","aa","kk","oo","mm","bb","aa","vv","kk","hh","hh","uu","ww","nf","aa","hh","pp","cc","ff","oo","gg","nn","ww","rr","bb","cc","ee","ff","ii","nn","pp","cc","kk","ee","kk","cc","tt","nn","vv","nf","yy","kk","ss","mm","kk","ff","kk","nn","ww","ll","ll","xx","hh","zz","vv","yy","zz","kk","xx","vv","ss","ee","ff","gg","hh","pp","yy","ii","qq","rf","ll","ss","gg","ll","bb","hh","vv","qq","bb","aa","ii","cc","ff","aa","cc","ee","qq","xx","ff","bb","fn","kk","tt","rr","vv","tt","dd","ss","kk","rf","ll","oo","aa","mm","xx","aa","ll","tt","nr","kk","vv"}));
        System.out.println(solution.longestPalindrome(new String[]{"gg"}));
        System.out.println(solution.longestPalindrome(new String[]{"gg","gg","gg"}));
        System.out.println(solution.longestPalindrome(new String[]{"gg","gg"}));

    }    
}

class SolutionLPBCTLW {
    public int longestPalindrome(String[] words) {

        HashMap<String , Integer> dictionary= new HashMap<String, Integer>();
        dictionary = counter(words);
        int countOfPairedMirrorWords=0;
        int countOfWordAtCenter =0;
        double countOfPairs=0;
        System.out.println(dictionary);
        
        for (String i : dictionary.keySet()){
            int countOfCurrentWord =dictionary.get(i);
            if (wordIsPalindromeOrNot(i)){
                // {aa : 3, gg: 2, ww:1}
                // It should be like        aaggaaggaa or aaggwwggaa
                countOfPairedMirrorWords += countOfCurrentWord/2 *2; // We can only take 2 so 3/2 =1*2 =2 
                if (countOfCurrentWord%2==1) countOfWordAtCenter =2; // It will always be one pair so no adding

            }else if (dictionary.containsKey(reversedString(i))){
                //if {ab :2, lw:1, wl:1, ty:1 yt:1}
                // lw + wl = 0.5+0.5 
                // ty + yt = 0.5 +0.5  because it will iterate through both
                countOfPairs+= Math.min(dictionary.get(i), dictionary.get(reversedString(i)))*0.5;
            }
        }
        return countOfPairedMirrorWords*2 +countOfWordAtCenter+ (int)countOfPairs*4;
        
    }
    public HashMap<String, Integer> counter(String[] words){
        HashMap<String , Integer> dictionary= new HashMap<String, Integer>();
        for (String i : words) dictionary.put(i, dictionary.getOrDefault(i, 0)+1);
        return dictionary;
    }

    public boolean wordIsPalindromeOrNot(String word){
        return (int)word.charAt(0) == (int) (word.charAt(1));
    }
    
    public String reversedString(String word){
        return ""+word.charAt(1)+word.charAt(0);
    }
}