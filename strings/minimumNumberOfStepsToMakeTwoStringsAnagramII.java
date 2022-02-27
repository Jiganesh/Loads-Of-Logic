// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

package strings;

import java.util.HashMap;

public class minimumNumberOfStepsToMakeTwoStringsAnagramII {
    public static void main(String[] args) {
        SolutionMNOSTMTWAII solution = new SolutionMNOSTMTWAII();
        System.out.println(solution.minSteps("leetcode", "coats"));
        System.out.println(solution.minSteps("adfhsk","dajfslkjfhakjshakhfkjashdfkjadsfakljsdfh"));
        
    }
}


class SolutionMNOSTMTWAII{

    // Submitted by Jiganesh

    // TC : O(S + T)
    // SC : O(sHashTable + tHashTable)

    // Runtime: 251 ms, faster than 33.33% of Java online submissions for Minimum Number of Steps to Make Two Strings Anagram II.
    // Memory Usage: 112.4 MB, less than 33.33% of Java online submissions for Minimum Number of Steps to Make Two Strings Anagram II.


    public int minSteps(String s, String t) {
        
        HashMap <Character,Integer> sHashMap = new HashMap<Character, Integer>();
        HashMap <Character,Integer> tHashMap = new HashMap<Character, Integer>();


        for(int i = 0 ; i<s.length(); i++){
            sHashMap.put(s.charAt(i) , sHashMap.getOrDefault(s.charAt(i),0)+1);
        }
        for(int i = 0 ; i<t.length(); i++){
            tHashMap.put(t.charAt(i) , tHashMap.getOrDefault(t.charAt(i),0)+1);
        }

        for (Character i : sHashMap.keySet()){
            if (tHashMap.containsKey(i)){
                tHashMap.put(i, (int)Math.abs(sHashMap.get(i)-tHashMap.get(i)));
            }else{
                tHashMap.put(i, sHashMap.get(i));
            }
        }

        int count  =0;
        for (Integer i : tHashMap.values()){
            count+=i;
        }
        return count;
    }

    // TC: O(S+T)
    // SC: O(1)

    // Runtime: 22 ms, faster than 100.00% of Java online submissions for Minimum Number of Steps to Make Two Strings Anagram II.
    // Memory Usage: 69.9 MB, less than 66.67% of Java online submissions for Minimum Number of Steps to Make Two Strings Anagram II.
   
    public int minStepsApproach2(String s, String t) {

        int count =0;
        int[] characterCount = new int[26];
        
        for (int i =0 ; i<s.length(); i++){
            // index = s.charAt(i)-'a'
            characterCount[s.charAt(i)-'a']++;
        }

        for (int i =0 ; i<t.length(); i++){
            // index = t.charAt(i)-'a'
            characterCount[t.charAt(i)-'a']--;
        }

        for (int i : characterCount){
            count += Math.abs(i);
        }
        return count;
    }
}

