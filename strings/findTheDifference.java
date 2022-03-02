// https://leetcode.com/problems/find-the-difference/

package strings;
import java.util.*;

public class findTheDifference {
    public static void main(String[] args) {
        
        SolutionFTD solution = new SolutionFTD();
        System.out.println(solution.findTheDifference("a", "aa"));
    }    
}

class SolutionFTD {

    // Submitted by @Jiganesh

    // TC : O(N+M)
    // SC : O(N)
    public char findTheDifference(String s, String t) {
        
        HashMap <Character, Integer> dictionary = new HashMap<Character,Integer>();
        
        for (int i = 0 ; i< s.length(); i++){
            dictionary.put(s.charAt(i), dictionary.getOrDefault(s.charAt(i),0)+1);
        }
        
        for (int i = 0 ; i< t.length(); i++){
            if (! dictionary.containsKey(t.charAt(i)) || dictionary.get(t.charAt(i))==0) return t.charAt(i);
            else dictionary.put(t.charAt(i),  dictionary.get(t.charAt(i))-1);
        }
        
        return ' '; 
    }

    // TC: O(N)
    // SC: O(1)

    public char findTheDifferenceApproach2(String s, String t) {
        
        int bit = 0;
        
        for (int i = 0 ; i<s.length(); i++){
            
            bit ^= 1 << s.charAt(i)-'a';
            bit ^= 1 << t.charAt(i)-'a';
        }
        
        bit ^= 1<< t.charAt(t.length()-1)-'a';
        
        int setbit = (int) (Math.log10(bit)/Math.log10(2));
        
        return (char)(setbit+(int)'a');
        
        
    }
}