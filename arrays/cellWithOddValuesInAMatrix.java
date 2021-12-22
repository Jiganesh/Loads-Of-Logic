package arrays;

import java.util.BitSet;

public class cellWithOddValuesInAMatrix {
    public static void main(String[] args) {
        int m =2;
        int n= 3;
        int [][] indices = new int[][] {{0,1},{1,1}};
        SolutionCWOVIAM solution = new SolutionCWOVIAM() ; 
        System.out.println(solution.oddCells(m,n,indices));

        int m1 =2;
        int n1= 2;
        int [][] indices1 = new int[][] {{1,1},{0,0}};
        
        System.out.println(solution.oddCells(m,n,indices));
        System.out.println(solution.oddCellsApproach2(m,n,indices));
        System.out.println(solution.oddCellsApproach3(m,n,indices));
        System.out.println(solution.oddCellsApproach4(m,n,indices));


        System.out.println(solution.oddCells(m1,n1,indices1));
        System.out.println(solution.oddCellsApproach2(m1,n1,indices1));
        System.out.println(solution.oddCellsApproach3(m1,n1,indices1));
        System.out.println(solution.oddCellsApproach4(m1,n1,indices1));


    }
    
}

class SolutionCWOVIAM {

    //TC : O((n+m)*L)+O(m*n) where L is length for indices
    //SC : O(m*n)
    public int oddCells(int m, int n, int[][] indices) {

        int [][] result = new int[m][n];

        for (int i =0 ;i< indices.length;i++){
            for (int j=0; j<n; j++){
                result[indices[i][0] ][j]++;
            }
            for (int j=0; j<m; j++){
                result[j][indices[i][1]]++;
            }
        }

        int count = 0;
        
        for (int i =0 ;i< m;i++){
            for (int j=0; j<n; j++){
                //System.out.print(result[i][j]+" ");
                count += (result[i][j]%2!=0)?1:0;
            }
            //System.out.println();
        }
        return count;
    }

    //TC : O(m*n)+O(L)
    //SC : O(m+n)

    public int oddCellsApproach2(int m , int n , int[][] indices){

        boolean[] rows = new boolean[m];
        boolean[] columns = new boolean[n];
        int count=0;
        for (int i=0; i< indices.length; i++){
            rows[indices[i][0]] ^= true;
            columns[indices[i][1]] ^= true;
        }

        for (int i =0; i<rows.length; i++){
            for(int j = 0 ; j< columns.length; j++){
                if (rows[i]^ columns[j]) count++;
            }
        }
        return count;

        // int r = countTrue(rows);
        // int c = countTrue(columns);
        
        // return r*n+c*m-2*r*c;
    }

    
    //TC : O(L+m+n)
    //SC : O(m+n)
    public int oddCellsApproach3(int m , int n , int[][] indices){

        boolean[] rows = new boolean[m];
        boolean[] columns = new boolean[n];

        for (int i=0; i< indices.length; i++){
            rows[indices[i][0]] ^= true;
            columns[indices[i][1]] ^= true;
        }


        int r = countTrue(rows);
        int c = countTrue(columns);
        
        return r*n+c*m-2*r*c;
    }

    public int countTrue(boolean[] array){
        int result =0;
        for (int i =0; i<array.length; i++){
            if (array[i]) result++;
        }
        return result;
    }

    //TC : O(L)
    //SC : O(m+n)
    public int oddCellsApproach4(int m, int n, int[][] indices) {
        BitSet oddRows = new BitSet(m), oddCols = new BitSet(n);
        int cntRow = 0, cntCol = 0;
        for (int[] idx : indices) {
            oddRows.flip(idx[0]);
            oddCols.flip(idx[1]);
            cntRow += oddRows.get(idx[0]) ? 1 : -1;
            cntCol += oddCols.get(idx[1]) ? 1 : -1;
        }
        return (n - cntCol) * cntRow + (m - cntRow) * cntCol;   
    }
}