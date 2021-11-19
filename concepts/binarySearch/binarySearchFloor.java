package concepts.binarySearch;

public class binarySearchFloor {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int target = 5;
        // Find the greatest element in array smaller than of equal to target


        System.out.println(floor(arr, target));
    }

    public static int floor(int[] array, int target) {
        int start = 0;
        int end = array.length-1;
        
        while(start<=end){
            int mid = start + (end-start)/2;
            if (array[mid]<target){
                start = mid +1;
            }else if (array[mid]>target){
                end = mid -1;
            }else {
                return array [mid];
            }
        }
        return array[end];

    }
}
