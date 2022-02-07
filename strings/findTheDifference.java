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
}