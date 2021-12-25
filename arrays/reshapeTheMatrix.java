// https://leetcode.com/problems/reshape-the-matrix/
package arrays;

import java.util.Arrays;

public class reshapeTheMatrix {
    public static void main(String[] args) {
        SolutionRTM solution = new SolutionRTM();
        int [][] mat = new int[][]{{1,2},{3,4}};
        //print(solution.matrixReshape(mat, 1, 4));
        //print(solution.matrixReshape(mat, 2, 4));
        print(solution.matrixReshape(mat, 4, 1));

        
    }
    public static void print(int[][]matrix){
        for (int[] i :matrix){
            System.out.println(Arrays.toString(i));
        }
    }
}

class SolutionRTM {
    public int[][] matrixReshape(int[][] mat, int r, int c) {

        int matRow = mat.length;
        int matCol = mat[0].length;

        if (matRow*matCol != r*c) return mat;
        int [][] outputArray = new int[r][c];

        int rowNum =0;
        int colNum =0;

        for (int i =0; i<matRow; i++){
            for (int j =0; j<matCol; j++){
                outputArray[rowNum][colNum] = mat[i][j];
                colNum++;
                if(colNum >= c){
                    colNum = 0;
                    rowNum++;
                }
            }
        }
        return outputArray;
    }
}

