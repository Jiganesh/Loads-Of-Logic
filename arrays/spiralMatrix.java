package arrays;

import java.util.*;

public class spiralMatrix {
    public static void main(String[] args) {
        SolutionSM solution = new SolutionSM();
        //System.out.println(solution.spiralOrder(new int[][]{{1,2,3},{4,5,6},{7,8,9}}));
        System.out.println(solution.spiralOrder(new int[][]{{1,2,3,4},{5,6,7,8},{9,10,11,12}}));

    }
}

class SolutionSM {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<Integer> ();
        return helper(matrix, 0 , matrix.length-1, 0, matrix[0].length-1, result); 
    }

    public List<Integer> helper(int[][] matrix, int startRow, int endRow, int startCol, int endCol, List<Integer> result) {
        
        if (startRow>endRow|| startCol > endCol) return result;
        
        //Right
        //Traverse till extreme Right;
        for (int col =startCol; col<=endCol; col++){
            result.add(matrix[startRow][col]);
        }

        //Down
        //Traverse from next row to last row 
        for(int row = startRow+1; row<=endRow; row++){
            result.add(matrix[row][endCol]);
        }

        //Left
        //Traverse in endrow from next endCol to startCol
        for (int col = endCol-1 ; col>=startCol; col--){
            result.add(matrix[endRow][col]);
        }

        //Up
        //Traverse from next above row to just below startRow
        for (int row=endRow-1; row>startRow; row--){
            result.add(matrix[row][startCol]);
        }

        return helper(matrix, startRow+1, endRow-1, startCol+1, endCol-1, result);
    }
}

