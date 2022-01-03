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
        
        int reachable =0;
        for (int i=0 ; i< nums.length; i++){
            if (i> reachable) break;
            reachable = Math.max(reachable, i + nums[i]);
            //System.out.println(reachable);
        }
        return reachable>=nums.length-1;        
    }
}
