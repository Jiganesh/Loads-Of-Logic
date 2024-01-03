

public class SolutionMNG {
    public int[] numberGame(int[] nums) {

        Arrays.sort(nums);
        int len = nums.length;
        int[] result = new int[len];


        for (int i = 0 ; i < len; i = i+2 ){
            result[i+1] = nums[i];
            result[i] = nums[i+1];
        }

        return result;
    }
}

