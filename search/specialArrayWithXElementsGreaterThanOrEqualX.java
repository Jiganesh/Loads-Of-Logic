package search;

import java.util.Arrays;

public class specialArrayWithXElementsGreaterThanOrEqualX{
    public static void main(String[] args) {
        SolutionSAWXEGTOEX solution = new SolutionSAWXEGTOEX();

        System.out.println(solution.specialArray(new int[]{3,5}));
        System.out.println(solution.specialArray(new int[]{0,0}));
        System.out.println(solution.specialArray(new int[]{0,4,3,0,4}));
        System.out.println(solution.specialArray(new int[]{3,6,7,7,0}));
        System.out.println(solution.specialArray(new int[]{3,9,7,8,3,8,6,6}));
        
    }  
}


class SolutionSAWXEGTOEX {

    // This approach takes nlogn time complexity
    public int specialArray(int[] nums) {
        Arrays.sort(nums); // nlog n
        int n = nums.length;
        
        for (int i =1; i<=n; i++){
            // Now we have to search for position of i
            int existingIndex = binarySearchLeftMostElementWithInDuplicates(nums, i); //logn

            // now we check how many numbers are greater than our i or current number 
            // using simple math we just subtract position from length of array to get how many numbers are ahead.
            if(nums.length-existingIndex == i)
                // if any number meets condition i.e
                // if numbers greater than i are equal to i we return that number
                {return i;}
            
        }
        return -1;
        
    }
    public int binarySearchLeftMostElementWithInDuplicates(int [] array, int target){
        int start = 0;
        int end = array.length-1;
        
        while(start<= end){
            int mid= start + (end -start)/2;
            if (array[mid]<target) start = mid +1;
            else if (array[mid]>=target) end =mid-1;
        }
        return start; 
    }
}



