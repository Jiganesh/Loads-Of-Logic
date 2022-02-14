package arrays;

import java.util.*;

public class contiguousArray{
    public static void main(String[] args) {
        SolutionCA solution = new SolutionCA();
        System.out.println(solution.findMaxLength(new int[]{0,1,0}));
        System.out.println(solution.findMaxLength(new int[]{0,1}));


    }
}
class SolutionCA {
    public int findMaxLength(int[] nums) {
      
        int len = nums.length;
        int min_1 = 0;
        int min_2 = 0;
        if(len < 2)
            return 0;
        for(int i=0;i<len;i++){
            if(nums[i] == 0){
                min_1 = 1;
                nums[i] = -1;
            }else
                min_2 = 1;
        }
        HashMap<Integer,Integer> al = new HashMap<Integer,Integer>();
        int ksm = 0;
        int max = Integer.MIN_VALUE;
        for(int i = 0;i<len;i++){

            ksm = ksm+nums[i];
            if(ksm == 0){
                if(max < (i+1))
                    max = i + 1;
            }

            if(al.get(ksm) == null)
            al.put(ksm,i);
            else{
                int dis = i - al.get(ksm);
                if(max < dis)
                    max = dis;
            }
        
        }
        
          if(min_1 >= 1 && min_2 >= 1)
          return max;
          else
          return 0;    
       
    }
}
