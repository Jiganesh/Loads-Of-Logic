package concepts.binarySearch;

import java.util.Arrays;

/*
Search in sorted matrix

Array is sorted Row wise and Column Wise 
eg:

{{10,20,30,40},
 {12,23,34,42},
 {14,26,36,45},
 {15,29,37,49}}

 Sorted in Rows and Columns like this, It does not stay sorted when they are flattened

{{01,03,05,07},
 {11,24,34,35},
 {37,38,46,48},
 {56,58,60,63}}

 Here Sorted array when flattened stays sorted. We are dealing with type 1 in this problem

*/
public class matrixSortedRowAndColumnWise {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(search(new int [][] {{10,20,30,40},
                                                                {12,23,34,42},
                                                                {14,26,36,45},
                                                                {15,29,37,49}}, 36)));
    }

    public static int [] search (int [][] matrix,int target){

        int row =0;
        int column = matrix[0].length-1;

        while(row<matrix.length && column>= 0){
            int pointingelement =matrix[row][column];
            if (pointingelement== target) return new int[]{ row, column};
            if (pointingelement < target) row++;
            else column--;
        }

        return new int[] {-1, -1};
    }
    
}
