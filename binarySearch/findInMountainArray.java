// https://leetcode.com/problems/find-in-mountain-array/

package binarySearch;
public class findInMountainArray {
    public static void main (String[] args){
        
        SolutionFIMA solution = new SolutionFIMA();

        System.out.println(solution.findInMountainArray(3,new int[]{1,2,3,4,5,3,1})); //2
        //3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

        System.out.println(solution.findInMountainArray(3, new int[]{0,1,2,4,2,1}));// -1
        //3 does not exist in the array, so we return -1.

        System.out.println(solution.findInMountainArray(3, new int[]{}));//-1
        //No element in array so -1
    }
}

class SolutionFIMA{
    
    int findInMountainArray(int target , int[] array){

        if (array.length >1){
            int peakIndex = peakAtIndex(array);
            int left = orderAgnosticBinarySearch(array, target,0, peakIndex); //leftside
            // searching element on left side and finding its index if it is not found return -1
            // left side of the peak will be sorted in a way so passing in order agnostic binary search
            if (left >-1) return left; // cause no need to search now in right side saving time


            int right = orderAgnosticBinarySearch(array, target,peakIndex+1, array.length-1); //rightside
            //searching element on right side also incase not found in left side
            //ride side of the peak will be sorted in a way so passing in order agnostic binary search
            if (right >-1) return right; // if inded found then it will return index or else it will return -1
            else return -1;
        }
        return -1;
    }

    int orderAgnosticBinarySearch(int[] array,int target , int start , int end){
        boolean isAsc = array[start]<array[end];
        while(start <= end){
            int mid = start +(end -start)/2;
            if (array[mid]==target) return mid;
            if (isAsc){
                if (array[mid]<target){
                    start = mid+1;
                }else if (array[mid]>target){
                    end = mid-1;
                }
            }else{
                if (array[mid]<target){
                    end = mid -1;
                }else if(array[mid]>target){
                    start = mid+1;
                }
            }
        }
        return -1;
    }

    int peakAtIndex(int [] array){
        int start =0;
        int end = array.length-1;

        while(start != end ){
            int mid = start + (end -start)/2;
            if (array[mid]<array[mid+1]) start = mid+1;
            else if (array[mid]> array[mid+1]) end = mid;
        }
        return start;
    }
}

// There are many calls to array[mid] optimize it by adding a variable to it.
