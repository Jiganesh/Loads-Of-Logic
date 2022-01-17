// https://leetcode.com/problems/word-pattern/
package strings;

import java.util.HashMap;
import java.util.HashSet;


public class wordPattern {
    public static void main(String[] args) {
        SolutionWP solution = new SolutionWP();
        System.out.println(solution.wordPattern("aba", "cat cat dog"));
    }
    
}

class SolutionWP {

    //  Submitted by @kushvr7

    public boolean wordPattern(String pattern, String s) {

        HashMap<Character, String> al = new HashMap<Character, String>();
        String[] rs = s.split(" ");
        char[] ch = pattern.toCharArray();        
        HashSet<String> set = new HashSet<String>();
        int ch_len = ch.length;
        int rs_len = rs.length;

        if(ch_len != rs_len)
             return false;

        for(int i=0;i<ch_len;i++){
            if(al.get(ch[i]) == null){
                if(set.contains(rs[i]))
                      return false;
                al.put(ch[i],rs[i]);
                set.add(rs[i]);
            }
            else if(al.get(ch[i]).equals(rs[i]) == false){
                return false;
            }

        }

        return true;
    }

    // Submitted by @Jiganesh

    //TC : O(N)
    //SC : O(N)
    // Runtime: 1 ms, faster than 86.67% of Java online submissions for Word Pattern.
    // Memory Usage: 37 MB, less than 71.95% of Java online submissions for Word Pattern.
    
    public boolean wordPatternApproach2(String pattern, String s) {

        char[] patternArray = pattern.toCharArray();
        String[] stringArray = s.split(" ");

        if (patternArray.length != stringArray.length) return false;
        
        HashSet <Object> setContainer = new HashSet<>();
       
        for (char i : patternArray) setContainer.add(i);
        int setPatternLength = setContainer.size();   
        setContainer.clear();

        for (String i: stringArray) setContainer.add(i);
        int setStringContainer= setContainer.size();
        setContainer.clear();

        if (setPatternLength!= setStringContainer) return false;

        HashMap<Character, String> dictionary = new HashMap<>();

        for (int i = 0 ; i< patternArray.length; i++){
            if( dictionary.containsKey(patternArray[i]) && !dictionary.get(patternArray[i]).equals(stringArray[i])){
                return false;
            }else{
                dictionary.put(patternArray[i], stringArray[i]);
            }
        }
        return true;   
    }
}