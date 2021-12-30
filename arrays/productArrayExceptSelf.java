package arrays;

import java.util.Arrays;

public class productArrayExceptSelf{
    public static void main(String[] args) {
        SolutionPAES solution = new SolutionPAES();
        solution.productExceptSelf(new int[]{1,2,3,4});
        solution.productExceptSelf(new int[]{-1,1,0,-3,3});

        solution.productExceptSelfApproach2(new int[]{1,2,3,4});
        solution.productExceptSelfApproach2(new int[]{-1,1,0,-3,3});
        
    }
}
class SolutionPAES {
    public int[] productExceptSelf(int[] nums) {

        int[] leftProduct = new int[nums.length];
        int[] rightProduct = new int[nums.length];

        leftProduct[0]=1;
        rightProduct[nums.length-1]=1;   
        
        for (int i=1; i< nums.length; i++){
            leftProduct[i]=leftProduct[i-1]*nums[i-1];
        }

        for(int i = nums.length-2; i>=0; i--){
            rightProduct[i]=rightProduct[i+1]*nums[i+1];
        }

        for (int i = 0 ; i< nums.length; i++){
            nums[i]=leftProduct[i]*rightProduct[i];
        }
        //System.out.println(Arrays.toString(leftProduct));
        //System.out.println(Arrays.toString(rightProduct));
        System.out.println(Arrays.toString(nums));
        return nums;
    }

    public int[] productExceptSelfApproach2(int[] nums){

        int[] outputArray = new int[nums.length];
        outputArray[0]=1;
        for (int i=1; i< nums.length; i++){
            outputArray[i]=outputArray[i-1]*nums[i-1];
        }

        int right =1;
        for(int i = nums.length-1; i>=0; i--){ 
            outputArray[i]=outputArray[i]*right;
            right*=nums[i];
        }
        
        //System.out.println(Arrays.toString(outputArray));;
        return nums;
    }
}