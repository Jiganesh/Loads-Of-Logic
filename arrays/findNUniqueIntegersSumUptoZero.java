package arrays;

import java.util.Arrays;

public class findNUniqueIntegersSumUptoZero {
    public static void main(String[] args) {
        SolutionFNUISUZ solution = new SolutionFNUISUZ();
        System.out.println(Arrays.toString(solution.sumZero(5)));
        System.out.println(Arrays.toString(solution.sumZero(4)));
        System.out.println(Arrays.toString(solution.sumZero(3)));
        System.out.println(Arrays.toString(solution.sumZero(1)));  
        
        System.out.println(Arrays.toString(solution.sumZeroApproach2(5)));
        System.out.println(Arrays.toString(solution.sumZeroApproach2(4)));
        System.out.println(Arrays.toString(solution.sumZeroApproach2(3)));
        System.out.println(Arrays.toString(solution.sumZeroApproach2(1)));  
    }
    
}

class SolutionFNUISUZ {

    //TC : O(N)
    //SC : O(N)
    public int[] sumZero(int n) {
        
        int start = 0;
        int end =n-1;
        int symmetric = n/2;

        int []  result = new int[n];
        while(start<=end){
            result[start]=-1*symmetric;
            result[end]=  symmetric;
            symmetric--;
            start++;
            end--;
        }
        return result; 
    }

    // Same TC and SC but efficient and easy to understand
    public int[] sumZeroApproach2(int n) {
        
        int[] result = new int[n];
        for(int i =1; i<n; i++){
            result[i-1]=i;
        }
        result[n-1]= (n-1)*(n)/2 *-1;
        return result;
    }


}
