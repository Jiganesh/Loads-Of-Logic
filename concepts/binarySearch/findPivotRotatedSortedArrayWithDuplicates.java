package concepts.binarySearch;

public class findPivotRotatedSortedArrayWithDuplicates {
    public static void main(String[] args) {
        int [] array = new int [] {4,4,5,6,7,8,8,8,1,2,3,4,};
        System.out.println(searchDuplicateSortedArray(array));
    }

    public static int  searchDuplicateSortedArray(int[] array){

        int start = 0;
        int end = array.length-1;

        while(start<=end){
            int mid = start +(end -start)/2;
            if (array[mid]> array[mid+1]) return mid;
            if (array[mid-1] > array[mid]) return mid-1;

            // if elements at middle, start, end are equal then just skip the duplicates
            if (array[mid] == array[start] && array[mid] == array[end]) {
                // skip the duplicates
                // NOTE: what if these elements at start and end were the pivot??
                // check if start is pivot
                if (start < end && array[start] > array[start + 1]) {
                    return start;
                }
                start++;

                // check whether end is pivot
                if (end > start && array[end] < array[end - 1]) {
                    return end - 1;
                }
                end--;
            }
            // left side is sorted, so pivot should be in right
            else if(array[start] < array[mid] || (array[start] == array[mid] && array[mid] > array[end])) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return -1;

    }
        
}


// 3 3 3 4 5 5 6 6 2 2 2 2 3
// s           m           e
//   s         m         e