// https://leetcode.com/problems/champagne-tower/

package dynamicProgramming;

public class champageneTower{
    public static void main(String[] args) {
        SolutionCT solution = new SolutionCT ();
        System.out.println(solution.champagneTower(2, 1, 1));
    }
}


class SolutionCT {

    // Submitted by Jiganesh


    // TC: O(N^2)
    // SC: O(N^2)

    // Simulating the situation


    // Runtime: 16 ms, faster than 36.07% of Java online submissions for Champagne Tower.
    // Memory Usage: 55.5 MB, less than 9.59% of Java online submissions for Champagne Tower.

    public double champagneTower(int poured, int query_row, int query_glass) {
        
        double[][] quantity = new double[101][101];
        
        quantity[0][0] = poured;
        
        for (int i = 0 ; i<=query_row; i++){
            for (int j =0; j<=query_glass ; j++){
                
                double rest = Math.max(quantity[i][j]-1.0, 0.0);
                quantity[i+1][j]+= rest/2.0;
                quantity[i+1][j+1]+= rest/2.0;
            }
        }
           
        return Math.min(quantity[query_row][query_glass],1.0);
        
    }
}

