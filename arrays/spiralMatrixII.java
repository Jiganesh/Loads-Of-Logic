package arrays;

import java.util.Arrays;

public class spiralMatrixII {

    public static void main(String[] args) {
        SolutionSMII solution = new SolutionSMII();
        int[][] result = solution.generateMatrix(3);
        for (int []i : result) System.out.println(Arrays.toString(i));
        
    }
    
}

class SolutionSMII{
    public int[][] generateMatrix(int n) {
        
        int[][] result = new int[n][n];
        int startRow= 0,startCol=0;
        int endRow =n-1, endCol=n-1;
        int counter =1;
        return helper(result, startRow, endRow, startCol , endCol, counter);
        
    }
    
    public int[][] helper(int[][] matrix, int startRow, int endRow, int startCol, int endCol, int counter){


        if (startRow > endRow && startCol > endCol) return matrix;

        for (int col = startCol ; col<= endCol; col++){
            matrix[startRow][col]= counter;
            counter++;
        }


        for (int row= startRow+1; row<= endRow; row++){
            matrix[row][endCol]= counter;
            counter++;
        }


        for (int col = endCol-1; col>=startCol ; col--){
            matrix[endRow][col] =counter;
            counter++;
        }


        for(int row = endRow-1 ; row>startRow; row--){
            matrix[row][startCol] = counter;
            counter++;
        }

        return helper(matrix, startRow+1, endRow-1, startCol+1, endCol-1, counter);
    }
}