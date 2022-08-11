package search;

public class searchA2DMatrixII {
    public static void main(String[] args) {
    SolutionSA2DMII solution = new SolutionSA2DMII();
    System.out.println(solution.searchMatrix(new int[][]{{1,4,7,11,15},{2,5,8,12,19},{3,6,9,16,22},{10,13,14,17,24},{18,21,23,26,30}},5));
    }
}

class SolutionSA2DMII {
    public boolean searchMatrix(int[][] matrix, int target) {
        
        int row = 0;
        int col = matrix[0].length-1;
        
        while(row<matrix.length && col>=0){
            int pointing = matrix[row][col];
            if (pointing == target) return true;
            else if ( pointing> target) col--;
            else row++;
        }
        
        return false;
        
    }
}