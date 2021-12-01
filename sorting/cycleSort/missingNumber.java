// https://leetcode.com/problems/missing-number/

package sorting.cycleSort;

public class missingNumber{
    public static void main(String[] args) {
        SolutionMN solution = new SolutionMN ();
        System.out.println(solution.missingNumber(new int[]{0,1}));
        System.out.println(solution.missingNumber(new int[] {3,0,1}));
    }
}

class SolutionMN {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int i = 0;
        while(i<n ){
            if(nums[i]==i || nums[i]==n) i++;
            else swap(nums, i, nums[i]);
        }
        for (int j = 0 ; j< n ; j++) if (nums[j] != j) return j;
        return n;
        
    }
    public void swap (int [] array , int currentIndex, int correctIndex){
        int temp= array[ correctIndex];
        array[correctIndex]= array[currentIndex];
        array[currentIndex]= temp;
        
    }
}

