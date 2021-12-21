package arrays;

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
        SolutionCWOVIAM solution1 = new SolutionCWOVIAM() ; 
        System.out.println(solution1.oddCells(m1,n1,indices1));
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
}