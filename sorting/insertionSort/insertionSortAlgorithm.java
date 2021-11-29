package sorting.insertionSort;

import java.util.Arrays;

public class insertionSortAlgorithm {

    public static void main(String[] args) {
        int [] array = new int []{9,6,1,6,9,2,3,7,10,-2,-6,-6,0};
        System.out.println(Arrays.toString(insertionSort(array)));
    
    }
    public static int[] insertionSort(int[] array){

        for (int i = 0; i<array.length; i++){
            int key = array[i];
            int j = i-1;

            while(j>=0 && array[j]> key){
                array[j+1]= array[j];
                j-=1;
            }
            array[j+1] = key;
        }
        return array;

    }
}

