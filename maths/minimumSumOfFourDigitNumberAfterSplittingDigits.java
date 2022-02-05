package maths;

import java.util.Arrays;

public class minimumSumOfFourDigitNumberAfterSplittingDigits {
    public static void main(String[] args) {
        SolutionMSOFDNASD solution = new SolutionMSOFDNASD();
        System.out.println(solution.minimumSum(4009));
        System.out.println(solution.minimumSum(2932));
        System.out.println(solution.minimumSum(5789));
        System.out.println(solution.minimumSum(2675));        
    }
}

class SolutionMSOFDNASD {

    // Submitted by @Jiganesh

    // TC :O(NlogN)
    // SC :O(N)
    public int minimumSum(int num) {

        int i = 0;
        int[] arr = new int[4];

        while (num > 0) {
            arr[i] = num % 10;
            num = num / 10;
            i++;
        }

        Arrays.sort(arr);
        return arr[0]*10 + arr[3] + arr[1]*10 +arr[2]; 
    }
}
