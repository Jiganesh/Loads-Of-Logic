package arrays;

public class partitionArrayAccordingToGivenPivot {
    public static void main(String[] args) {
        SolutionPAATGP solution = new SolutionPAATGP() ;
        System.out.println(solution.pivotArray(new int[]{9,12,5,10,14,3,10}, 10));
    }
}

class SolutionPAATGP {

    // Submitted by @ Jiganesh

    // TC : O(N)
    // SC : O(N)

    // Runtime: 3 ms, faster than 100.00% of Java online submissions for Partition Array According to Given Pivot.
    // Memory Usage: 55.2 MB, less than 100.00% of Java online submissions for Partition Array According to Given Pivot.
    
    public int[] pivotArray(int[] nums, int pivot) {
        
        int [] result = new int[nums.length];
        int pointer = 0;
        
        for (int num: nums){
            if (num<pivot) {
                result[pointer]= num;
                pointer++;
            }
        }
        
        for (int num: nums){
            if (num==pivot) {
                result[pointer]= num;
                pointer++;
            }
        }
        
        for (int num: nums){
            if (num>pivot) {
                result[pointer]= num;
                pointer++;
            }
        }
        
        return result;
        
    }
}


