// https://leetcode.com/problems/find-in-mountain-array/

public class FindInMountainArray {
    public static void main (String[] args){
        
        SolutionFIMA solution = new SolutionFIMA();

        System.out.println(solution.findInMountainArray(3,new int[]{1,2,3,4,5,3,1})); //2
        //3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

        System.out.println(solution.findInMountainArray(3, new int[]{0,1,2,4,2,1}));// -1
        //3 does not exist in the array, so we return -1.
    }
}

class SolutionFIMA{
    
    int findInMountainArray(int target , int[] array){

        return -1;
    }
}



