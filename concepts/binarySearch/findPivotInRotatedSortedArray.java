package concepts.binarySearch;

// find the pivot (as pivot here will always be largest element in array in rotated sorted array)
// For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

public class findPivotInRotatedSortedArray {

    public static void main(String[] args) {
        System.out.println(findPivot(new int[] {1,3}));
        System.out.println(findPivot(new int[] {4,5,6,7,0,1,2}));     

        // if there is no pivot that means if array is not rotated it will return -1;
    }
    
    static int findPivot(int[] array) {
        int start = 0 ;
        int end = array.length -1 ;
        
        while(start <=end){
            int mid = start +(end - start )/2;
            //case 1 and case 2 
            if (mid <end && array[mid]>array[mid+1]) return mid;
            if (mid >start && array[mid -1]> array [mid]) return mid -1;
            
            //case 3
            if(array[start]<=array[mid]) start = mid +1;
            else end = mid -1 ;
        }
        return -1;
    }
}
