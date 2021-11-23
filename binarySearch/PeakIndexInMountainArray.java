// https://leetcode.com/problems/peak-index-in-a-mountain-array/
// https://leetcode.com/problems/find-peak-element/

// Two Questions but same Answer

package binarySearch;
public class PeakIndexInMountainArray {
    public static void main(String[] args) {
        

        SolutionPIIMA solution = new SolutionPIIMA();
        // This Arrays are also called as Bitonic Array
        // It is first sorted in Ascending Order and Descending Order
        System.out.println(solution.peakIndexInMountainArray(new int []{2,3,5,7,6,2,1}));
        System.out.println(solution.peakIndexInMountainArray(new int []{0,2,1,0}));
        System.out.println(solution.peakIndexInMountainArray(new int []{0,10,5,2}));
        System.out.println(solution.peakIndexInMountainArray(new int []{24,69,100,99,79,78,67,36,26,19}));
    }
}
class SolutionPIIMA {
    public int peakIndexInMountainArray(int[] array) {

        int start =0;
        int end = array.length-1;

        while(start != end){
            int mid = start + (end -start )/2;

            if (array[mid]<array[mid+1]) start = mid +1;
            else if(array [mid]> array[mid+1]) end = mid ;

        }
        return start;       
    }
}

/*

ROUGH WORK

0 1 2 3 4 5 6 7 8 9
2 3 4 5 6 7 8 2 1 0
s       m         e

if middle element has next element greater than itself then answer must lie ahead
so start = mid +1

if middle element has next element lesser than itself answer must lie to left including that number
so end = mid




*/