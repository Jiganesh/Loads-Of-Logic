// https://leetcode.com/problems/lucky-numbers-in-a-matrix/

package arrays;

import java.util.ArrayList;
import java.util.List;

public class luckyNumbersInAMatrix {
    public static void main(String[] args) {
        SolutionLNIAM solution = new SolutionLNIAM();
        System.out.println(solution.luckyNumbers(new int [][]{{3,7,8},{9,11,13},{15, 16,17}}));
        System.out.println(solution.luckyNumbers(new int [][]{{7,8},{1,2}}));
        System.out.println(solution.luckyNumbers(new int [][]{{1,10,4,2},{9,3,8,7},{15,16,17,12}}));

    }
}

class SolutionLNIAM {
    public List<Integer> luckyNumbers (int[][] matrix) {
        List <Integer> result = new ArrayList<Integer> ();
        
        
        for (int row =  0 ; row< matrix.length; row++){
            int minNumberInColIndex =0;
            for(int numberIndex = 0 ; numberIndex <matrix[row].length; numberIndex++){
                if(matrix[row][minNumberInColIndex] > matrix[row][numberIndex]) {
                    minNumberInColIndex= numberIndex;
                }
            }
            //System.out.println(minNumberInColIndex);
            //System.out.println("current Minimum in Row : "+matrix[row][minNumberInColIndex]);
            
            int maxInCol = matrix[row][minNumberInColIndex];
            for(int colSearchIndex= 0 ; colSearchIndex<matrix.length; colSearchIndex++){
                if(matrix[row][minNumberInColIndex]<matrix[colSearchIndex][minNumberInColIndex]){
                    maxInCol = matrix[colSearchIndex][minNumberInColIndex];
                }
                //System.out.println("Traversing Through col to search max in col : "+ matrix[colSearchIndex][minNumberInColIndex]);
            }
            if(maxInCol == matrix[row][minNumberInColIndex]) result.add(maxInCol);
        }
        return result;  
    }
}
