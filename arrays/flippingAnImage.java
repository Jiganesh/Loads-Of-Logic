package arrays;
import java.util.Arrays;

public class flippingAnImage {
    public static void main(String[] args) {
        SolutionFAI solution = new SolutionFAI();
        int[][] result = (solution.flipAndInvertImage(new int[][] {{1,1,0},{1,0,1},{0,0,0}}));
        for(int[]i: result){
            System.out.println(Arrays.toString(i));
        }
    }
}


class SolutionFAI {

    //TC : O(N^2)
    //SC : O(N^2)

    // Runtime on Leetcode 0ms and 100% faster
    public int[][] flipAndInvertImage(int[][] image) {
        
        int [][] result = new int[image.length][image[0].length];

        for(int i = 0 ; i< image.length; i++){
            int [] row = new int[image[0].length];
            for (int j = 0 ; j< image[i].length; j++){
                row[image[i].length-j-1]=(image[i][j]==1)?0:1;
            }
            result[i]= row;
        }

        return result;
        
    }
}