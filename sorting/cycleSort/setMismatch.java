// https://leetcode.com/problems/set-mismatch/
package sorting.cycleSort;

public class setMismatch {
    public static void main(String[] args) {
        SolutionSM solution = new SolutionSM();
        System.out.println(solution.findErrorNums(new int[]{1,2,2,4}));
        System.out.println(solution.findErrorNums(new int[]{3,2,3,4,5,6}));
        System.out.println(solution.findErrorNums(new int[]{1,1}));
        System.out.println(solution.findErrorNums(new int[]{2,2}));


        
    }
    
}

class SolutionSM {
    public int[] findErrorNums(int[] nums) {

        int i = 0;
        // sort the array with count sort 
        while (i< nums.length){ 
            if(nums[i]==i+1 || nums[nums[i]-1]==nums[i]) i++;            
            else swap(nums, i , nums[i]-1);
        }
        // Check through array find the index with wrong number in place
        for (int j = 0 ; j < nums.length; j++){
            if(nums[j] !=j+1) return new int[]{nums[nums[j]-1], j+1};

            // return {correct Index of Duplicate Number , Number which was duplicated it will be index +1}
            // nums[nums[j]-1] will give which number is duplicate 
            // j+1 will give what correct number should be present at duplicated value/ wrong value
        }
        return new int []{-1,-1};
        
    }
    public void swap (int [] nums, int currentIndex, int correctIndex){
        int temp = nums[correctIndex];
        nums[correctIndex]= nums[currentIndex];
        nums[currentIndex]= temp;
    }
}