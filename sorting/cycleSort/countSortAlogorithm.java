package sorting.cycleSort;

import java.util.Arrays;

// when given numbers are from range 1.........N use countSort
public class countSortAlogorithm {

    public static void main(String[] args) {
        int [] array = new int [] {9,2,1,3,4,8,6,7,5,10};
        System.out.println(Arrays.toString(countSort(array)));
    }

    public static int[] countSort(int [] array ){

        int i = 0;
        while(i<array.length){
            if(array[i]!=i+1){
                int correct = array[i]-1;
                swap (array,i, correct);
            }else i++;
        }
        return array;
    }
    public static void swap(int[] array ,int i , int j){
        int temp = array[i];
        array[i]= array[j];
        array[j]=temp;
    }
    
}
