package arrays;

import java.util.HashSet;

public class checkIfEveryRowAndColumnContainsAllNumbers{
    public static void main(String[] args) {
        SolutionCIERACCAN solution = new SolutionCIERACCAN();
        System.out.println(solution.checkValid(new int[][]{{1,2,3},{3,1,2},{2,3,1}}));
        System.out.println(solution.checkValid(new int[][]{{1,1,1},{3,1,2},{2,3,1}}));
        System.out.println(solution.checkValid(new int[][]{{1,2,3},{2,1,2},{3,3,1}}));
        
    }
}

class SolutionCIERACCAN {
    public boolean checkValid(int[][] matrix) {

        HashSet<Integer> row = new HashSet<Integer>();
        HashSet<Integer> column = new HashSet<Integer>();

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                row.add(matrix[i][j]);    // row Hashset will have all the elements in that row
                column.add(matrix[j][i]); // column Hashset will have all the elements in that column
            }

            for (int p =1; p<=matrix.length; p++){
                //checking if the number is present in current row as well as current column
                if (!row.contains(p) || !column.contains(p)) return false;
            }
            row.clear();
            column.clear();
        }
        return true;
        
    }
}