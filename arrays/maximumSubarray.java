package arrays;

public class maximumSubarray {
    public static void main(String[] args) {
        SolutionMSA solution = new SolutionMSA();
        System.out.println(solution.maxSubArray(new int []{1})); //1
        System.out.println(solution.maxSubArray(new int []{-2,1,-3,4,-1,2,1,-5,4})); //6
        System.out.println(solution.maxSubArray(new int []{5,4,-1,7,8})); //23

    }
    
}

class SolutionMSA {
    public int maxSubArray(int[] nums) {
        
        int maxSum = nums[0];
        int currentSum = nums[0];
        
        for (int i = 1; i< nums.length; i++){
            currentSum = Math.max(currentSum+nums[i], nums[i]);
            maxSum = Math.max(currentSum, maxSum);
        }
        return maxSum;
        
    }
}