// https://leetcode.com/problems/find-all-duplicates-in-an-array/

package sorting.cycleSort;

import java.util.ArrayList;
import java.util.List;

public class findAllTheDuplicatesInAnArray {

    public static void main(String[] args) {
        SolutionFATDIAA solution = new SolutionFATDIAA();
        System.out.println(solution.findDuplicates(new int[]{4,3,2,7,8,2,3,1}));
        System.out.println(solution.findDuplicates(new int[] {1,1,2}));
    }
}
class SolutionFATDIAA {
    public List<Integer> findDuplicates(int[] nums) {
        
        List<Integer> result = new ArrayList<Integer>();
        
        int i = 0;
        while(i< nums.length){
            if(nums[i] != i+1){ 
                if(nums[nums[i]-1] == nums[i]) i++;
                else swap (nums, i, nums[i]-1);
            }else{
                i++;
            }
        }
        for(int j = 0 ; j < nums.length; j++){
            if(nums[j]!=j+1) result.add(nums[j]);
        }
        return result;
    }
    
    public void swap (int [] nums, int currentIndex , int correctIndex){
        int temp = nums[correctIndex];
        nums[correctIndex] = nums[currentIndex];
        nums[currentIndex] = temp;
    }
}
