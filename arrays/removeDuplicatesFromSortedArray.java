package arrays;

public class removeDuplicatesFromSortedArray {
    public static void main(String[] args) {
        SolutionRDFSA solution = new SolutionRDFSA();
        System.out.println(solution.removeDuplicatesApproach2(new int[]{0,0,1,1,1,2,2,3,3,4}));
        System.out.println(solution.removeDuplicatesApproach2(new int[]{1,2,3,4}));
        System.out.println(solution.removeDuplicatesApproach2(new int[]{1,1,2}));
        System.out.println(solution.removeDuplicatesApproach2(new int[]{1}));
        System.out.println(solution.removeDuplicatesApproach2(new int[]{}));


    }
}

class SolutionRDFSA {
    public int removeDuplicates(int[] nums) {
        
        int i =0;
        int j =0;
        
        while(j< nums.length){
            while(j< nums.length && nums[i]==nums[j]) j++;
            i++;
            if(j< nums.length) nums[i]=nums[j];

        }
        
        return i;
    }


    // TC: O(N)
    // SC: O(1)
    public int removeDuplicatesApproach2(int[] nums) {
        
        int i =0;
        for (int j = 0 ; j< nums.length ; j++){
            if(i<nums.length && j<nums.length &&nums[i]!=nums[j]){
                nums[++i]=nums[j];
            }
        }
        return i+1;
    }
}
