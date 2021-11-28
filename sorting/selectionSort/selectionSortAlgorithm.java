package sorting.selectionSort;

import java.util.Arrays;

public class selectionSortAlgorithm {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(selectionSort(new int [] {5, 2, 4, 6, 1, 3})));
        System.out.println(Arrays.toString(selectionSort(new int [] {-1,-3,0,4,7,8,10,12})));
        System.out.println(Arrays.toString(selectionSort(new int [] {4,-3,12,-8,23,9,-1,-1,-1,2})));
    }

    public static int[] selectionSort(int[] array){
        int n = array.length-1;

        for(int i = 0; i<n; i++){
            int key = i;
            for(int j = i+1; j<=n; j++){

                
                if(array[key]>= array[j]){
                    key =j;
                }
            }
            int temp = array[i];
            array[i]= array[key];
            array[key] = temp;

        }
        return array;
    }
}
