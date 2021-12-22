package strings;

// https://leetcode.com/problems/adding-spaces-to-a-string/

import java.util.ArrayList;

public class addingSpacesToAString {
    public static void main(String[] args) {
        SolutionASTTS solution = new SolutionASTTS();
        System.out.println(solution.addSpaces("icodeinpython",new int[]{1,5,7,9}));
        System.out.println(solution.addSpaces("spacing", new int[] {0,1,2,3,4,5,6}));
        System.out.println(solution.addSpaces("LeetcodeHelpsMeLearn", new int[]{8,13,15}));

        System.out.println(solution.addSpacesApproach2("icodeinpython",new int[]{1,5,7,9}));
        System.out.println(solution.addSpacesApproach2("spacing", new int[] {0,1,2,3,4,5,6}));
        System.out.println(solution.addSpacesApproach2("LeetcodeHelpsMeLearn", new int[]{8,13,15}));

    }
    
}

class SolutionASTTS {

    //Runtime: 1239 ms
    public String addSpaces(String s, int[] spaces) {
        
        StringBuilder result = new StringBuilder(s);
        int count=0;
        for (int i: spaces){
            
            result.insert(i+count, ' ');
            count+=1;
        }
        return result.toString();
    }

    // Runtime : 12 ms
    // TC : O (m+n)
    // SC : O (m+n)
    public String addSpacesApproach2(String s, int[] spaces){

        int spacesTracker = 0;
        int resultTracker =0;
        int i =0;
        char[] result  = new char[s.length()+spaces.length];
        int count=0;
        while (i< s.length()){

            if(spacesTracker < spaces.length && spaces[spacesTracker]+count==resultTracker){
                count++;
                result[resultTracker]=   ' ';
                result[resultTracker+1]= s.charAt(i);
                resultTracker+=2;
                spacesTracker++;
        
            }else {
                result[resultTracker]= s.charAt(i);
                resultTracker++;

            }
            i++;
        }
        return new String(result);
    }

    // Runtime : 43ms
    // TC : O(N)
    // SC : O(N^2)
    public String addSpacesApproach3(String s, int[] spaces) {
        
        ArrayList<String> array = new ArrayList<>();
        int start=0;
        for (int i: spaces){
            
            array.add(s.substring(start,i));
            start =i;
        }
        array.add(s.substring(start));

        return String.join(" ", array);
    }

}
