// https://leetcode.com/problems/3sum/
package arrays;

import java.util.*;
public class threeSum{
    public static void main(String[] args) {

        SolutionThreeSum solution = new SolutionThreeSum ();
        System.out.println(solution.threeSum(new int[]{-1,0,1,2,-1,-4}));
        System.out.println(solution.threeSum(new int[]{}));
        System.out.println(solution.threeSum(new int[]{3,0,-2,-1,1,2}));
        System.out.println(solution.threeSum(new int[]{0}));
        System.out.println(solution.threeSum(new int[]{0,0,0,0}));

        System.out.println(solution.threeSumApproach2(new int[]{-1,0,1,2,-1,-4}));
        System.out.println(solution.threeSumApproach2(new int[]{}));
        System.out.println(solution.threeSumApproach2(new int[]{3,0,-2,-1,1,2}));
        System.out.println(solution.threeSumApproach2(new int[]{0,0}));
        System.out.println(solution.threeSumApproach2(new int[]{0,0,0,0}));
        System.out.println(solution.threeSumApproach2(new int[]{-2,0,1,1,2}));
        
    }
}

class SolutionThreeSum {

    // BruteForce Approach
    
    // TC: O(N^3)
    // SC :O(N)
    public List<List<Integer>> threeSum(int[] nums) {


        HashSet<List<Integer>> resultSet = new HashSet<List<Integer>>();
        List<List<Integer>> result = new ArrayList<List<Integer>>();

        
        Arrays.sort(nums);


        for (int i = 0 ; i< nums.length; i++){
            for (int j =i+1; j<nums.length; j++){
                for (int k = j+1; k< nums.length; k++){

                    if (nums[i]+nums[j]+nums[k] == 0){
                        resultSet.add(Arrays.asList(new Integer[]{nums[i], nums[j], nums[k]}));
                    }
                }
            }
        }

        for (List<Integer> i: resultSet){
            result.add(i);
        }
        
        return result;  
    }


    // TC: O(N^2)
    // SC : O(N)
    
    // Runtime: 18 ms, faster than 95.11% of Java online submissions for 3Sum.
    // Memory Usage: 45.8 MB, less than 86.22% of Java online submissions for 3Sum.

    public List<List<Integer>> threeSumApproach2(int[] nums) {

        List<List<Integer>> result = new ArrayList<List<Integer>>();


        Arrays.sort(nums);
        for (int i = 0 ; i< nums.length ; i++){

            if (i> 0 && nums[i]==nums[i-1]) continue;

            int j = i+1;
            int k = nums.length-1;

            while (j < k){

                if (nums[i]+nums[j]+nums[k] > 0 ) k--;
                else if (nums[i]+nums[j]+nums[k]<0) j++;
                else{

                    result.add(Arrays.asList(new Integer[]{nums[i],nums[j], nums[k]}));

                    while (j<k && nums[j]==nums[j+1]) j++;
                    while (j<k && nums[k]==nums[k-1]) k--;
                    j++;
                    k--;

                    
                }
            }

        }
        return result;

    }
}
