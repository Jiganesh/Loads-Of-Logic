package arrays;

import java.util.Arrays;

public class spiralMatrixIII{
    public static void main(String[] args ){

        SolutionSMIII solution = new SolutionSMIII();
        int [][]result = solution.spiralMatrixIII(5, 6, 1 , 4);
        print(result);

    }

    public static void print(int[][] matrix){
        for (int[] i:matrix) System.out.println(Arrays.toString(i)+" ");
    }
}

class SolutionSMIII{
    public int[][] spiralMatrixIII(int rows, int cols, int rStart, int cStart) {

        int [][] result = new int[rows*cols][2];
        int pointerInMatrix =0;
        result[pointerInMatrix++] = new int[]{rStart, cStart}; 

        int len =0;
        int direction =0;
        int [] directions = new int[]{0,1,0,-1,0};

        while(pointerInMatrix< rows*cols){
            if(direction==0 || direction==2){
                len++;
            }
            for(int k =0; k< len; k++){
                rStart += directions[direction];
                cStart += directions[direction+1];
                if(isValid(rStart, cStart, rows, cols)) result[pointerInMatrix++]= new int[] {rStart, cStart};
            }

            direction= ++direction%4;
        }
        return result;        
    }
    public boolean isValid(int rStart, int cStart, int rows, int cols){

        return rStart<rows && rStart>=0 && cStart<cols && cStart>=0;

    }
}