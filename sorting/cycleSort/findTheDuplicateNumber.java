// https://leetcode.com/problems/find-the-duplicate-number/

package sorting.cycleSort;

public class findTheDuplicateNumber {
    public static void main(String[] args) {
        SolutionFTDN solution = new SolutionFTDN();
        System.out.println(solution.findDuplicate(new int[]{1,3,4,2,2}));
        System.out.println(solution.findDuplicate(new int[]{1,1,2}));
    }
}

class SolutionFTDN {
    public int findDuplicate(int[] nums) {
        
        int i = 0;
        while(i< nums.length){
            
            if(nums[i] != i+1) {
                int correctIndexOfele = nums[i]-1;
                if(nums[correctIndexOfele] != nums[i]) swap(nums, i , correctIndexOfele);
                else return nums[i];
            }else{
                i++;
            }
        }
        return -1;
    }
    
    public void swap(int[] nums, int currentIndex, int correctIndex){
        int temp = nums[correctIndex];
        nums[correctIndex]= nums[currentIndex];
        nums[currentIndex]= temp;
    }
}