class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
       
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
