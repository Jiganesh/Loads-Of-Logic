package maths;
// https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class SolutionFindNumbersWithEvenNumbersOfDigit {
    public int findNumbers(int[] nums) {
        
        int count =0;
        for (int num : nums){
            if (num<0) num = num*-1; 
            if ( ((int) Math.log10(num)+1) %2==0) count++;
        }
        return count;  
    }
}
public class findNumbersWithEvenNumberOfDigits {
    public static void main(String[] args) {
        SolutionFindNumbersWithEvenNumbersOfDigit solution = new SolutionFindNumbersWithEvenNumbersOfDigit();
        int[] nums = {12,345,2,6,7896};
        System.out.println(solution.findNumbers(nums));

        int[] nums1 = {-23, 00, -343, -343483};
        System.out.println(solution.findNumbers(nums1));

    } 
}
