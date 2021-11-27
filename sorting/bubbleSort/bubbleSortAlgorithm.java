package sorting.bubbleSort;
import java.util.Arrays;

public class bubbleSortAlgorithm {
    public static void main(String[] args) {
        int [] array = {9,10,8,7,6,5,1,2,3,0};
        System.out.println(Arrays.toString(bubbleSort(array)));
    }

    public static int[] bubbleSort(int [] array){

        int n = array.length;
        for (int i =0 ; i<n; i++ ){
            for (int j =1; j<n-i; j++){
                if (array[j-1]>=array[j]){
                    int temp = array[j-1];
                    array[j-1] = array[j];
                    array[j]= temp;
                }
            }
        }

        return array;
    }
}

/*

Time Complexity :
Best Case : O(n)
Worst Case :O(n^2) 

Space Complexity: O(1)
That is why it is also called Inplace Sorting Algorithm

When the original order is maintained for the values that are equal that is stable sorting.
Bubble Sort in stable sorting Algorithm

*/
