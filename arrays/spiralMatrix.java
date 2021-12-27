package arrays;

import java.util.*;

public class spiralMatrix {
    public static void main(String[] args) {
        SolutionSM solution = new SolutionSM();
        System.out.println(solution.spiralOrder(new int[][]{{1,2,3},{4,5,6},{7,8,9}}));
        System.out.println(solution.spiralOrder(new int[][]{{1,2,3,4},{5,6,7,8},{9,10,11,12}}));
        System.out.println(solution.spiralOrder(new int[][]{{6,9,7}}));


    }
}

class SolutionSM {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<Integer> ();
        return helper(matrix, 0 , matrix.length-1, 0, matrix[0].length-1, result); 
    }

    public List<Integer> helper(int[][] matrix, int startRow, int endRow, int startCol, int endCol, List<Integer> result) {
        
        while (startRow<=endRow&& startCol <=endCol){
        
        //Right
        //Traverse till extreme Right;
        for (int col =startCol; col<=endCol; col++){
            result.add(matrix[startRow][col]);
        }
        startRow++;

        //Down
        //Traverse from next row to last row 
        for(int row = startRow; row<=endRow; row++){
            result.add(matrix[row][endCol]);
        }
        endCol--;

        //Left
        //Traverse in endrow from next endCol to startCol
        if(startRow <= endRow){
            for (int col = endCol ; col>=startCol; col--){
                result.add(matrix[endRow][col]);
            }
        }
        endRow--;

        

        //Up
        //Traverse from next above row to just below startRow
        if(startCol<=endCol){
            for (int row=endRow; row>=startRow; row--){
            result.add(matrix[row][startCol]);
            }
        }
        startCol++;

    }

        return result;
    }
}

