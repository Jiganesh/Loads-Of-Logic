
package search;

//https://leetcode.com/problems/search-a-2d-matrix/

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


// Watch Kunal Kushwaha's Video for Understanding 
// https://www.youtube.com/watch?v=
// Jump to 22:00

import java.util.*;

public class searchA2DMatrix {
    public static void main(String[] args) {
        SolutionSA2DM  solution = new SolutionSA2DM();
        System.out.println(solution.searchMatrix(new int[][] {{1,3,5,7},{10,11,16,20},{23,30,34,60}}, 3));
        System.out.println(solution.searchMatrix(new int[][] {{1,3,5,7},{10,11,16,20},{23,30,34,60}},13));
        System.out.println(solution.searchMatrix(new int [][]{{1,3,5,7},{10,11,16,20},{23,30,34,60}},13));
        System.out.println(solution.searchMatrix(new int[][]{{1},{3}}, 3));
    }    
}


class SolutionSA2DM {
    // Submitted by Jiganesh
    public boolean binarySearch (int [][] matrix , int row, int cStart, int cEnd, int target){
    
            while (cStart <= cEnd){
                int cMid = cStart + (cEnd -cStart)/2;
                if (matrix[row][cMid]== target) return true;
                else if (matrix[row][cMid]< target) cStart = cMid+1;
                else cEnd = cMid-1;
            }
            return false;
        }
        public boolean searchMatrix (int[][] matrix, int target) {
    
            int rows = matrix.length;
            int cols = matrix[0].length-1;
    
            if(rows ==1) return binarySearch(matrix, rows-1, 0, cols, target);
    
            int rStart = 0;
            int rEnd = matrix.length-1;
    
            int cMid = matrix[0].length/2;
            while(rStart<(rEnd-1)){
                int rMid = rStart  + (rEnd - rStart)/2;
                if (matrix[rMid][cMid]== target) return true;
                else if (matrix [rMid][cMid]< target) rStart = rMid;
                else rEnd= rMid;
            }
    
            if(target < matrix[rStart][cMid]) return binarySearch(matrix, rStart, 0, cMid-1, target);
            if(target >= matrix[rStart][cMid] && target <= matrix[rStart][cols]) return binarySearch(matrix, rStart, cMid, cols, target);
            
            if(target >=matrix[rEnd][0]&& target<= matrix[rEnd][cMid])  return binarySearch(matrix, rEnd, 0, cMid, target) ;  
            if(target> matrix[rEnd][cMid]) return binarySearch(matrix, rEnd, cMid+1, cols, target) ;  
             return false;
        }

        //Submitted by @kushvr
        public boolean searchMatrixApproach2(int[][] matrix, int target) {

            int rlen = matrix.length;
            int clen = matrix[0].length;
    
            for(int i=0;i<rlen;i++){
                if(matrix[i][0] <= target && matrix[i][clen - 1] >= target){
                    int ind = Arrays.binarySearch(matrix[i],target);
                    if(ind >= 0)
                        return true;
                }
            }
            return false;
        }
    }