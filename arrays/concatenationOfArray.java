package arrays;
// https://leetcode.com/problems/concatenation-of-array/ 

public class concatenationOfArray {
    public static void main(String[] args) {
        SolutionCOA solution = new SolutionCOA ();
        System.out.println(solution.getConcatenation(new int[]{1,3,2,1}));
    }
    
}

class SolutionCOA {
    public int[] getConcatenation(int[] nums) {
        int[] result = new int[nums.length*2];
        for (int i=0; i<=nums.length-1; i++){
            //result[i] = nums[i%nums.length];
            //One way to do it

            //Other way
            result[i] = result[nums.length+1] = nums[i];
        }
        return result;
        
        
    }
}