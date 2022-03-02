// https://leetcode.com/problems/number-of-matching-subsequences/
package hashTable;
import java.util.*;

public class numberOfMatchingSubsequences {

    public static void main(String[] args) {

        SolutionNOMS solution =new SolutionNOMS();
    System.out.println(solution.numMatchingSubseq("dsahjpjauf", new String[] {"ahjpjau","ja","ahbwzgqnuk","tnmlanowax"}));
        
    }
    
}



class SolutionNOMS{


    // Submitted by Jiganesh

    // TC :O(N*M)
    // SC : O(N)
    
    public int numMatchingSubseq(String s, String[] words) {
        
        int count=0;
        
        HashMap<String, Integer> wordDictionary = new HashMap<String, Integer> ();
        
        for (String t : words){
            wordDictionary.put(t, wordDictionary.getOrDefault(t, 0)+1);
        }
        
        
        for (String t : wordDictionary.keySet()){
            if (isSubsequence(t, s)) count += wordDictionary.get(t);
        }
        return count;
    }
    
    
    public boolean isSubsequence(String childString, String parentString) {

        int pointerOnS = childString.length()-1;
        int pointerOnT = parentString.length()-1;


        while(pointerOnT >= 0 && pointerOnS>=0){

            if(parentString.charAt(pointerOnT) != childString.charAt(pointerOnS)){
                pointerOnT--;
            }else{
                pointerOnS--;
                pointerOnT--;
            }
            
        }

        return pointerOnS<0;
    }
}