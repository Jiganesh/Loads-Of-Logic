package concepts.binarySearch;

public class binarySearchCeiling {
    public static void main(String[] args){
        int [] array = new int[] {1,3,4,5,8,10,12,23,45,67,78,89};
        int target = 89;
        // Find the smallest element in array greater than of equal to target

        System.out.println(ceiling(array,target));
    }

    public static int ceiling(int[]array, int target){

        int start =0;
        int end =array.length-1;
    

        if (target>array[end]) return -1;


        while (start<= end){
            int mid = start + (end-start)/2;
            if(array[mid]<target){
                start = mid+1;
            }else if (array[mid]>target){
                end = mid-1;
            }else{
                return array[mid];
            }
        }

        return array[start];
    }
} 