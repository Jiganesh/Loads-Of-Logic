package search;
// https://leetcode.com/problems/find-peak-element/
public class findPeakElement {
    public static void main(String[] args) {
        SolutionPE solution = new SolutionPE();
        System.out.println(solution.findPeakElement(new int []{1,2,1,3,5,6,4}));
        System.out.println(solution.findPeakElement(new int []{1,2,3,1}));
        System.out.println(solution.findPeakElement(new int []{1}));
        System.out.println(solution.findPeakElement(new int []{6,5,4,3,2,3,2}));
    }
}


class SolutionPE{
    public int findPeakElement(int[] array) {
        
        int start = 0;
        int end= array.length -1;
        
        while(start != end ){
            int mid = start + (end - start)/2;
            if (array[mid]< array[mid+1]) start = mid +1;
            else end = mid;
        }
        return start;
    }
}