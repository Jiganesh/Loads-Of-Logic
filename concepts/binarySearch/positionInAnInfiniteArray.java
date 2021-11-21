package concepts.binarySearch;

// Amazon Question available on GFG
public class positionInAnInfiniteArray {
    public static void main(String[] args) {
        int [] array = new int [] {0,1,2,3,4,5,6,7,8,9,10};
        int target = 4;
        System.out.println(infiniteBinarySearch(array,target));
    }

    public static int infiniteBinarySearch(int[] array, int target){

        int start = 0;
        int end = 1;

        while(target > array[end]){
            int newStart = end +1;
            end = end +(end -start+1)*2;
            start = newStart;
        }
        return binarySearch(array, start, end, target);
    }

    public static int binarySearch(int[] array, int start, int end , int target){

        while (start <= end){
            int mid = start +(end - start )/2;
            if (array[mid]==target) return mid;
            else if (array[mid]<target) start = mid +1;
            else end = mid -1;
        }
        return -1;

    }
}
