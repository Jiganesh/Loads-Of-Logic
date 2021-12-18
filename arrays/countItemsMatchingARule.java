package arrays;

import java.util.ArrayList;
import java.util.List;

public class countItemsMatchingARule {
    public static void main(String[] args) {
        SolutionCIMAR solution = new SolutionCIMAR();

        List<List<String>> items = new ArrayList<List<String>>();
        List<String> item1 = new ArrayList <String>();
        item1.add("phone"); item1.add("blue"); item1.add("pixel");
        items.add(item1);


        List<String> item2 = new ArrayList <String>();
        item2.add("computer"); item2.add("silver"); item2.add("phone");
        items.add(item2);

        List<String> item3 = new ArrayList <String>();
        item3.add("phone"); item3.add("gold"); item3.add("iphone");
        items.add(item3);

        String ruleKey= "type";
        String ruleValue ="phone";
        System.out.println(solution.countMatches(items, ruleKey, ruleValue));
    }
    
}

class SolutionCIMAR {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        
        int check = (ruleKey.equals( "type"))? 0: (ruleKey.equals("color")) ?1 :2;
        int count =0;
        
        for (List <String> i : items){
            if (i.get(check).equals(ruleValue)) count++;
        }
        return count;
    }
}

/* 

Input: items = [["phone","blue","pixel"],
                ["computer","silver","phone"],
                ["phone","gold","iphone"]], 
ruleKey = "type", ruleValue = "phone"

Output: 2
Explanation: There are only two items matching the given rule, 
which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. 
Note that the item ["computer","silver","phone"] does not match.

*/