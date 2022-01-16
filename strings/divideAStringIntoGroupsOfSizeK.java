// https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/
package strings;

import java.util.ArrayList;

public class divideAStringIntoGroupsOfSizeK {
    public static void main(String[] args) {

        SolutionDASIGOSK solution = new SolutionDASIGOSK();
        solution.divideString("abcdefghi", 3, 'x');
        solution.divideString("abcdefghij", 3, 'x');
        
    }
}

class SolutionDASIGOSK {
    public String[] divideString(String s, int k, char fill) {

        ArrayList<String> arrayList = new ArrayList<String>();
        
        int lengthOfString = s.length();

        // Filling the string with given fill character if the string is short
        if(lengthOfString%k !=0) s = fillString(s,fill,k-(lengthOfString%k));

        int i = 0;
        while(i < lengthOfString){
            arrayList.add(s.substring(i, i+k));
            i+=k;
        }

        System.out.println(arrayList);
        return arrayList.toArray(new String[arrayList.size()]);
        
    }
    public String fillString (String s , char fill , int fillTimes){

        StringBuilder sb= new StringBuilder(s);
        
        while (fillTimes-->0){
            sb.append(fill);
        }
        return sb.toString();

    }
}