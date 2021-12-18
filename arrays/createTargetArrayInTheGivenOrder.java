package arrays;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class createTargetArrayInTheGivenOrder {
    public static void main(String[] args) {

        SolutionCTAITGO solution = new SolutionCTAITGO();
        int[] result = solution.createTargetArray(new int[] { 0, 1, 2, 3, 4 }, new int[] { 0, 1, 2, 2, 1 }); // [0, 4,
                                                                                                             // 1, 3, 2]
        System.out.println(Arrays.toString(result));

        int[] resultApproach2 = solution.createTargetArrayApproach2(new int[] { 0, 1, 2, 3, 4 },
                new int[] { 0, 1, 2, 2, 1 }); // [0, 4, 1, 3, 2]
        System.out.println(Arrays.toString(resultApproach2));

    }

}

class SolutionCTAITGO {

    // TC : O(N^2)
    // SC : O(N)
    public int[] createTargetArray(int[] nums, int[] index) {

        List<Integer> list = new ArrayList<Integer>();
        for (int i = 0; i < nums.length; i++) {
            list.add(index[i], nums[i]);
        }

        int[] arr = list.stream().mapToInt(i -> i).toArray();
        return arr;
    }

    // TC : O(N^2)
    // SC : O(N)
    public int[] createTargetArrayApproach2(int[] nums, int[] index) {

        int[] result = new int[nums.length];
        Arrays.fill(result, -1);
        for (int i = 0; i < nums.length; i++) {
            if (index[i] < i) insertAt(result, index[i], nums[i]);
            else result[index[i]] = nums[i];
        }
        return result;
    }

    public void insertAt(int[] result, int index, int target) {

        for (int i = result.length-1; i>index; i--){
            result[i]= result[i-1];
        }
        result[index]= target;
    }

}