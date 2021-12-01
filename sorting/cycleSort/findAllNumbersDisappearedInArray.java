// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/

package sorting.cycleSort;
import java.util.*;

public class findAllNumbersDisappearedInArray {
    public static void main(String[] args) {
        SolutionFANDIA solution = new SolutionFANDIA();
        System.out.println(solution.findDisappearedNumbers(new int[]{4,3,2,7,8,2,3,1}));
        System.out.println(solution.findDisappearedNumbers(new int []{1,1}));
        
    }
    
}

class SolutionFANDIA {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> result = new ArrayList<Integer>();
        int i = 0; 
        while(i< nums.length){
            int numberAtIndexi = nums[i];
            int correctIndexOfi= nums[i]-1;
            if(numberAtIndexi!= nums[correctIndexOfi])swap(nums, i, correctIndexOfi);
            else i++;
        }
        for (int j = 0 ; j< nums.length ; j++){
            if (nums[j]-1!= j) result.add(j+1);
        }
    
        return result;
        
    }
    public void swap(int[] nums, int currentIndex, int correctIndex){
        int temp = nums[correctIndex];
        nums[correctIndex]=nums[currentIndex];
        nums[currentIndex] = temp;
    }
}