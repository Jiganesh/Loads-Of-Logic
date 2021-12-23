package arrays;

public class determineWhetherMatrixCanBeObtainedByRotation {
    public static void main(String[] args) {
        SolutionDWMCBOBR solution = new SolutionDWMCBOBR();
        System.out.println(solution.findRotation(new int[][]{{0,1},{1,0}}, new int[][]{{1,0},{0,1}}));
        System.out.println(solution.findRotation(new int[][]{{0,1},{1,1}}, new int[][]{{1,0},{0,1}}));
        System.out.println(solution.findRotation(new int[][]{{0,0,0},{0,1,0},{1,1,1}}, new int[][]{{1,1,1},{0,1,0},{0,0,0}}));
    }
}

class SolutionDWMCBOBR {
    public boolean findRotation(int[][] mat, int[][] target) {

        for (int i=0 ; i<4 ; i++){
            if( check (mat , target)) return true;
            else rotate (mat);
        }
        return false;
    }

    public void rotate(int[][] mat){

        for(int i =0; i< mat.length; i++){
            for(int j =0; j<i; j++){
                int temp = mat[i][j];
                mat[i][j]=mat[j][i];
                mat[j][i]= temp;
            }
        }
        //for (int[] i : mat) System.out.println(Arrays.toString(i));
        //System.out.println("Transpose done");

        int start =0;
        int end = mat[0].length-1;

        while(start< end){
            for (int i=0; i< mat.length; i++){
                int temp = mat[i][start];
                mat[i][start]= mat[i][end];
                mat[i][end]= temp;
            }
            start++;
            end --;
        }
        //for (int[] i : mat) System.out.println(Arrays.toString(i));
        //System.out.println("Rotation done");
        
    }

    public boolean check (int [][] mat , int[][] target){
        for (int i =0 ; i< mat.length; i++){
            for(int j = 0 ; j< mat[i].length ; j++){
                if (mat[i][j]!=target[i][j]) return false;
            }
        }
        return true;
    }
}