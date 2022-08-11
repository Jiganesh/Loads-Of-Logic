package search;

//https://leetcode.com/problems/kth-missing-positive-number/

public class kthMissingPositiveNumber {
    public static void main(String[] args) {
        SolutionKMPN solution = new SolutionKMPN();
        System.out.println(solution.findKthPositive(new int [] {2,3,4,7,11}, 5));   
        System.out.println(solution.findKthPositive(new int [] {1,2,3,4}, 2));    
 
    }
}

class SolutionKMPN {
    public int findKthPositive(int[] arr, int k) {
        int start = 0;
        int end = arr.length-1;

        while (start <= end ){
            int mid = start + (end - start)/2;
            if( arr[mid]- (mid+1)<k) start= mid+1;
            else if (arr[mid]-(mid+1)>k) end = mid-1;
        }
        return k+end+1;

        
    }
}