package arrays;

public class jumpGame {
    public static void main(String[] args) {
        SolutionJG solution = new SolutionJG();
        System.out.println(solution.canJump(new int[]{2,3,1,1,4}));
        System.out.println(solution.canJump(new int[]{3,2,1,0,4}));
        
    }
}


class SolutionJG {
    public boolean canJump(int[] nums) {
        
        int jump=0;
        for (int i = 0; i<nums.length; i++){
            if (jump<nums.length)jump+=nums[i];
            if( jump==nums.length-1) return true;
            else jump-=nums[i];
        }
        return jump==nums.length-1;
        
    }
}
