// https://leetcode.com/problems/transpose-matrix/
package arrays;

public class transposeMatrix {
    public static void main(String[] args) {
        SolutionTM solution = new SolutionTM() ;
        print(solution.transpose(new int[][]{{1,2,3},{4,5,6},{7,8,9}}));
        print(solution.transpose(new int[][]{{1,2,3},{4,5,6}}));   

    }

    public static void print(int[][] matrix){
        for (int[] i : matrix){
            for(int j : i){
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }
}

class SolutionTM {
    public int[][] transpose(int[][] matrix) {

        int[][] result = new int[matrix[0].length][matrix.length];
        
        for(int i=0; i< matrix.length; i++){
            for (int j =0 ; j<matrix[i].length;j++){
                result[j][i]= matrix[i][j];
                
            }
        }
        return result;
        
    }
    
}