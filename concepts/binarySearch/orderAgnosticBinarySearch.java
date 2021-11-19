package concepts.binarySearch;

public class orderAgnosticBinarySearch{
    public static void main(String[] args) {
        int [] array = new int[] {-100, -30, -10 ,-4, 0, 0 ,1 ,3,6,7,12,45,70,100};
        System.out.println(orderAgnosticBS(array, 7));
    }

    public static int orderAgnosticBS(int [] array, int target){

        int start =0;
        int end = array.length-1;

        boolean isAscending = array[start]<array[end];

        while (start <= end){
            int mid = start + (end - start)/2;

            if (isAscending){

                if (array[mid]<target) {
                    start = mid+1;
                }else{
                    end = mid-1;
                }
            
            }else{
                if (array[mid]>target){
                    start = mid +1;
                }else{
                    end = mid -1;
                }
            }
            if (array[mid]==target ) return mid;

        }
        return -1;
    }
}
