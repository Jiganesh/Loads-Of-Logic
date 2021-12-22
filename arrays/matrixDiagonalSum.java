package arrays;

public class matrixDiagonalSum{
    public static void main(String[] args) {
        SolutionMDS solution = new SolutionMDS();
        System.out.println(solution.diagonalSum(new int[][]{{1,2,3},{4,5,6},{7,8,9}} ));
        System.out.println(solution.diagonalSum(new int[][]{{1,1,1,1},{1,1,1,1},{1,1,1,1},{1,1,1,1}}));
    }
}


class SolutionMDS {

    //BruteForce
    public int diagonalSum(int[][] mat) {
        if (mat.length <=0) return -1;
        int startCol= 0;
        int endCol = mat[0].length-1;
        int primaryDiaEle=0, secondaryDiaEle =0, sum =0;

        for (int row =0; row<mat.length; row++){
            primaryDiaEle = mat[startCol][row];
            secondaryDiaEle = (startCol!=endCol) ? mat[endCol][row]:0;
            startCol++;
            endCol--;

            //System.out.println (primaryDiaEle + " "+secondaryDiaEle );
            sum+= (primaryDiaEle +secondaryDiaEle );
        }
        return sum;
    }

    //TC : O(N)
    //SC : O(1)
    public int diagonalSumApproach2(int[][] mat) {
        
        if (mat.length <=0) return -1;
        int startCol= 0;
        int endCol = mat[0].length-1;
        int sum =0 , n = mat.length;

        for (int row =0; row<n; row++){
            sum += mat[startCol][row]+ mat[endCol][row];
            startCol++;
            endCol--;
        }
        return (n%2!=0) ? sum-mat[n/2][n/2] : sum;
    }

    //TC : O(N)
    //SC : O(1)
    public int diagonalSumApproach3(int[][] mat) {
        int res = 0;
        int n = mat.length;
        for (int i=0; i<n; i++) {
            res += mat[i][i]; // Primary diagonals are row = column! 
            res += mat[n-1-i][i]; // Secondary diagonals are row + column = n-1!
        }
        return n % 2 == 0 ? res : res - mat[n/2][n/2]; // if n is a odd number, that mean we have added the center element twice!
    }
}