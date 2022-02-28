// https://leetcode.com/problems/summary-ranges/
package arrays;

import java.util.*;

public class summaryRanges{
    public static void main(String[] args) {

        SolutionSR solution = new SolutionSR();
        System.out.println(solution.summaryRanges(new int[]{0,1,2,4,5,7}));
        System.out.println(solution.summaryRanges(new int[]{0,2,3,4,6,8,9}));

        
    }
}

class SolutionSR {

    // Submitted by Jiganesh

    // TC : O(N)
    // SC : O(P*M) Where P is length of List and M is lenght of String
    
    // Runtime: 0 ms, faster than 100.00% of Java online submissions for Summary Ranges.
    // Memory Usage: 42.2 MB, less than 29.79% of Java online submissions for Summary Ranges. 

    public List<String> summaryRanges(int[] nums) {
        List<String> result = new ArrayList<String> ();

        if (nums.length ==0) return result;
        int start = nums[0];
        StringBuilder sb = new StringBuilder();

        for (int i =1 ; i< nums.length; i++){
            if (nums[i]-nums[i-1] !=1){
                
                if (start != nums[i-1]){
                    sb.append(start);
                    sb.append("->");
                    sb.append(nums[i-1]);
                }else{
                    sb.append(start);
                }
                start = nums[i];
                result.add(new String(sb));
                sb.setLength(0);
            }
        }
    
        if (start != nums[nums.length-1] ){
            sb.append(start);
            sb.append("->");
            sb.append(nums[nums.length-1]);
        }else{
            sb.append(start);
        }
        result.add(new String(sb));
        return result; 
    }    

    // Modified and Aesthetic Code
    public List<String> summaryRangesApproach2(int[] nums) {

        int n = nums.length;
        List<String> result = new ArrayList<String> ();

        if (n ==0) return result;
        int start = nums[0];

        for (int i =1 ; i< nums.length; i++){
            if (nums[i]-nums[i-1] !=1){

                if (start != nums[i-1]){
                    result.add( start + "->"+ nums[i-1]);
                }else{
                    result.add(start+"");
                }
                start = nums[i];  
            }
        }

        if (start != nums[n-1]){
            result.add( start + "->"+ nums[n-1]);
        }else{
            result.add(start+"");
        }
        return result;
    }
}


// Extra Notes: 
// I'll vote for sb.setLength(0); not only because it's one function call, 
// but because it doesn't actually copy the array into another array like sb.delete(0, builder.length()); 
// It just fill the remaining characters to be 0 and set the length variable to the new length.