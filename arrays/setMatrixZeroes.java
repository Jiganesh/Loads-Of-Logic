package arrays;

// Solution Idea : https://www.youtube.com/watch?v=zgaOU5aInOc
// Improved this solution

// Question : https://leetcode.com/problems/set-matrix-zeroes/submissions/
import java.util.Arrays;
import java.util.HashSet;

public class setMatrixZeroes {
    public static void main(String[] args) {
        SolutionSMZ solution = new SolutionSMZ();
        int[][] matrix1 = new int[][] { { 1, 1, 0 }, { 1, 1, 1 }, { 1, 1, 1 } };
        int[][] matrix2 = new int[][] { { 0, 1, 2, 0 }, { 3, 4, 5, 2 }, { 1, 3, 1, 5 } };

        solution.setZeroesApproach3(matrix1);
        print(matrix1);
        solution.setZeroesApproach3(matrix2);
        print(matrix2);

    }

    public static void print(int[][] matrix) {
        for (int[] i : matrix)
            System.out.println(Arrays.toString(i));

    }
}

class SolutionSMZ {
    // Time Complexity : O(n*m)* (n+m)
    // If all number are positives even for Integer.MIN_VALUE it wont work
    // Space Complexity : O(1)
    public void setZeroes(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {

                if (matrix[row][col] == 0) {
                    for (int i = 0; i < matrix[0].length; i++) {
                        if (matrix[row][i] != 0)
                            matrix[row][i] = -1;
                    }

                    for (int i = 0; i < matrix.length; i++) {
                        if (matrix[i][col] != 0)
                            matrix[i][col] = -1;
                    }
                }
            }
        }

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {

                if (matrix[row][col] == -1)
                    matrix[row][col] = 0;

            }
        }
    }

    public int[][] setZeroesApproach2(int[][] matrix) {

        // Faster than 52% , less Space than 50%. (LeetCode)
        int rl = matrix.length;
        int cl = matrix[0].length;

        HashSet<Integer> x = new HashSet<Integer>(); // In order to save rows duplication , so that we dont check the row which is already 0 by another cell
        HashSet<Integer> y = new HashSet<Integer>(); // In order to save column duplication.

        for (int i = 0; i < rl; i++) {
            for (int j = 0; j < cl; j++) {
                if (matrix[i][j] == 0) {
                    x.add(i);
                    y.add(j);
                }
            }
        }

        for (int r_pos : x) {
            for (int j = 0; j < cl; j++) matrix[r_pos][j] = 0;
        }

        x.clear();

        for (int c_pos : y) {
            for (int j = 0; j < rl; j++) matrix[j][c_pos] = 0;
        }

        y.clear();
        return matrix;
    }

    // Time Complexity : O(n*m)
    // Space Complexity : O(n+m)
    public void setZeroesApproach3(int[][] matrix) {

        int[] rowTracker = new int[matrix.length];
        int[] colTracker = new int[matrix[0].length];

        for (int row = 0; row < matrix.length; row++) {
            for (int col = 0; col < matrix[0].length; col++) {
                if (matrix[row][col] == 0) {
                    rowTracker[row] = -1;
                    colTracker[col] = -1;
                }
            }
        }

        for (int row = 0; row < matrix.length; row++) {
            for (int col = 0; col < matrix[0].length; col++) {
                if (rowTracker[row] == -1 || colTracker[col] == -1)
                    matrix[row][col] = 0;

            }
        }
    }

    // Time Complexity : O(N*M)
    // Space Complexity : O(1)
    public void setZeroesApproach4(int[][] matrix) {

        boolean inRow = false;
        boolean inCol = false;

        int rows = matrix.length;
        int cols = matrix[0].length;

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {

                // checking if any zero in any row and changing boolean inRow so we can change
                // whole row to zero
                if (row == 0 && matrix[0][col] == 0)
                    inRow = true;
                // checking if any zero in any col and changing boolean inCol so we can change
                // whole col to zero
                if (col == 0 && matrix[row][0] == 0)
                    inCol = true;
                // if any zero in separated array changing row and col for that
                if (row > 0 && col > 0 && matrix[row][col] == 0) {
                    matrix[row][0] = 0;
                    matrix[0][col] = 0;
                }
            }
        }

        for (int row = rows - 1; row >= 0; row--) {
            for (int col = cols - 1; col >= 0; col--) {

                // Traversing from back so we do not make any change to stored values in row =0
                // and col =0
                // as we are using them to keep track
                if (inRow && row == 0)
                    matrix[0][col] = 0;
                if (inCol && col == 0)
                    matrix[row][0] = 0;
                if (matrix[0][col] == 0 || matrix[row][0] == 0)
                    matrix[row][col] = 0;
            }
        }
    }
}
