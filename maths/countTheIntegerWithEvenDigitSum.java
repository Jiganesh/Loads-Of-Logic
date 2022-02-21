// https://leetcode.com/problems/count-integers-with-even-digit-sum/

package maths;

public class countTheIntegerWithEvenDigitSum {
    public static void main(String[] args) {

        SolutionCTIWEDS solution = new SolutionCTIWEDS();
        System.out.println(solution.countEven(10));
        System.out.println(solution.countEven(20));
        System.out.println(solution.countEven(30));

    }
}


class SolutionCTIWEDS {

    // Submitted by @Jiganesh

    // Runtime: 0 ms, faster than 100.00% of Java online submissions for Count Integers With Even Digit Sum.
    // Memory Usage: 40.8 MB, less than 50.00% of Java online submissions for Count Integers With Even Digit Sum.
    
    // Efficient Approach

    //TC : O(n) where n in length of the given number
    //SC : O(1)

    public int countEven(int num) {
        
        int temp = num;
        int sumOfNumDigits = 0;
        
        while (num>0){
            sumOfNumDigits+= num%10;
            num/=10;
        }
        
        return (sumOfNumDigits%2==0) ? temp/2 : (temp-1)/2;
        
    }
}