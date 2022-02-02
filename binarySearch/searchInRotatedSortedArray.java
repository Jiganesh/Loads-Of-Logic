package binarySearch;
public class searchInRotatedSortedArray {
    public static void main(String[] args) {

        SolutionSISA solution = new SolutionSISA();

        System.out.println(solution.search(new int[] { 4, 5, 6, 7, 0, 1, 2 }, 0)); // 4
        System.out.println(solution.search(new int[] { 4, 5, 6, 7, 0, 1, 2 }, 3)); // -1
        System.out.println(solution.search(new int[] { 1, 3 }, 0)); // -1
        System.out.println(solution.search(new int[] { 1 }, 1)); // 0
        System.out.println(solution.search(new int[] { 1, 3 }, 1)); // 0
        System.out.println(solution.search(new int[] { 1, 3 }, 3)); // 1

    }
}

class SolutionSISA {
    public int search(int[] nums, int target) {
        int pivot = findPivot(nums);
        if(pivot ==-1) return binarySearch(nums, target,0, nums.length-1);
        if(target>=nums[0]) return binarySearch(nums,target, 0 , pivot);
        else return binarySearch(nums,target, pivot+1, nums.length-1);
        
    }

    public int binarySearch(int[] array , int target , int start , int end){
        while(start<=end){
            int mid = start +(end -start);
            if(array[mid]<target) start = mid +1;
            else if(array[mid]>target) end = mid-1;
            else return mid;
        }
        return -1;
    }
    
    public int findPivot(int[] array){
        int start = 0 ;
        int end = array.length -1 ;
        
        while(start <=end){
            int mid = start +(end - start) /2;
            //case 1 and case 2 
            if (mid >start && array[mid -1]> array [mid]) return mid -1;
            if (mid <end && array[mid]>array[mid+1]) return mid;
            
            //case 3
            if(array[start]<=array[mid]) start = mid +1;
            else end = mid -1 ;
        }
        return -1;
    }
}
