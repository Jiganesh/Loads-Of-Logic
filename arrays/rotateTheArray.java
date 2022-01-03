package arrays;

// https://leetcode.com/problems/rotate-array/
public class rotateTheArray {
    public static void main(String[] args) {
        SolutionRA solution = new SolutionRA();
        
        int [] array1 =new int[]{1,2,3,4,5,6,7};
        solution.rotate(array1, 3);
        printIntegers(array1);

        int [] array2 = new int[]{-1,-100,3,99};
        solution.rotate(array2, 2);
        printIntegers(array2);   
        
        int [] array3 = new int[]{-1};
        solution.rotate(array3, 2);
        printIntegers(array3); 
        
    }

    public static void printIntegers(int [] array){
        for (int i : array) System.out.print(i+ " ");
        System.out.println();
    }
}

class SolutionRA {
    public void rotate(int[] nums, int k) {
        k =k%nums.length; // 1 2 3 4 5 6 7
        reverse(nums, 0, nums.length-k-1);   // 4 3 2 1 5 6 7 
        reverse(nums, 0, nums.length-1); // 7 6 5 1 2 3 4
        reverse(nums, 0, k-1); // 5 6 7 1 2 3 4 

    }

    public void reverse (int [] nums, int start , int end){
        while(start <end){
            int temp = nums[start];
            nums[start]= nums[end];
            nums[end]=temp;
            start++;
            end--;
        }
    }
}