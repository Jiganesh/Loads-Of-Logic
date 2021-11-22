package concepts.binarySearch;

// find the pivot (as pivot here will always be largest element in array in rotated sorted array)
// For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

public class findPivotInRotatedSortedArray {

    public static void main(String[] args) {
        int [] array= new int []{4,5,6,7,0,1,2};
        System.out.println(pivot(array));     
    }
    
    public static int pivot (int[] array){

        int start = 0;
        int end = array.length-1;

        while (start != end){
            int mid = start + (end -start)/ 2;
            if (array[mid]> array[mid+1]) return mid;
            if (array[start] < array[mid]) end= mid;
            else start = mid;
        }
        return -1;
    }
}
