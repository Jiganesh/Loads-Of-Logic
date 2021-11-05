class SolutionTwoSumII {
    public int[] twoSum(int[] numbers, int target) {
        
        int start = 0 ;
        int end =  numbers.length-1;
        
        while (start<end){
            if (numbers[start]+numbers[end]== target){
                return new int []{start+1,end+1};
            }else if (numbers[start]+numbers[end] > target){
                end--;
            }else{
                start++;
            }
        }
        return new int[]{-1,-1};
    }
}

public class TwoSumII {
    public static void main(String[] args) {
        SolutionTwoSumII s = new SolutionTwoSumII();
        int[] nums = {2,7,11,15};
        int target = 9;
        int[] result = s.twoSum(nums, target);
        System.out.println(result[0]+" "+result[1]);
    }
}
