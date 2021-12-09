package binarySearch;

public class countNegatives{
    public static void main(String[] args) {

        SolutionCN solution = new SolutionCN();
        System.out.println(solution.countNegatives(new int[][]{{4,3,2,-1},{3,2,1,-1},{1,1,-1,-2},{-1,-1,-2,-3}}));
        
    }
}

class SolutionCN {
    public int countNegatives(int[][] grid) {
        int row  =0 ;
        int column = grid [row].length-1;
        
        int total = 0;
        while (row <= grid.length-1 ){
            if (column >=0 && grid[row][column]<0) {
                //System.out.println(grid[row][column]);
                column--;
                total++;
            }
            else {
                column = grid [row].length-1;
                row++; 
            }
            
        }
        return total;   
    }
}