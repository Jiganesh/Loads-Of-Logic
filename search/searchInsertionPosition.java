package search;

public class searchInsertionPosition {
    public static void main(String[] args) {
        SolutionSIP solution =new SolutionSIP();
        System.out.println(solution.searchInsert(new int[]{1,3,5,6}, 2)); //1
        System.out.println(solution.searchInsert(new int[]{1,3,5,6}, 5)); //2
        
    }
}

class SolutionSIP {
    public int searchInsert(int[] nums, int target) {
        int start = 0;
        int end = nums.length-1;
        
        while (start <=end){
            int mid = start + (end -start )/2;
            if(target<nums[mid]) end = mid-1;
            else if (target > nums[mid]) start = mid+1;   
            else return mid;
        }
        return start;
    }
}