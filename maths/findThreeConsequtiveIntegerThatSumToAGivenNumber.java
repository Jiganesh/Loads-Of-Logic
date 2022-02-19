package maths;

import java.util.Arrays;

public class findThreeConsequtiveIntegerThatSumToAGivenNumber {
    public static void main(String[] args) {
        SolutionFTCITSTAGN solution = new SolutionFTCITSTAGN();
        print(solution.sumOfThree(33));
        print(solution.sumOfThree(0));
        print(solution.sumOfThree(1));
    }
    public static void print(long[] arr) {
        System.out.println(Arrays.toString(arr));
    }
}


class SolutionFTCITSTAGN {
    public long[] sumOfThree(long num) {
        
        long d = (num-3)/3;
        return (d*3+3 == num)? new long[]{d, d+1,d+2} : new long[0];
    }
}