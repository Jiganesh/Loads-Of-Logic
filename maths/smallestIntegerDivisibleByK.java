// https://leetcode.com/problems/smallest-integer-divisible-by-k/

package maths;

import java.math.BigInteger;
import java.util.HashSet;

public class smallestIntegerDivisibleByK{
    public static void main(String[] args) {
        SolutionSIDBK solution = new SolutionSIDBK();
        System.out.println(solution.smallestRepunitDivByK(1));
        System.out.println(solution.smallestRepunitDivByK(3));
        System.out.println(solution.smallestRepunitDivByK(23));
        System.out.println(solution.smallestRepunitDivByK(49993));

        System.out.println(solution.smallestRepunitDivByKApproach2(1));
        System.out.println(solution.smallestRepunitDivByKApproach2(3));
        System.out.println(solution.smallestRepunitDivByKApproach2(23));
        System.out.println(solution.smallestRepunitDivByKApproach2(49993));

    }
}

class SolutionSIDBK {
    //BruteForce
    // TC : O(N) where N is length of the number which is divisible by k
    // SC : O(1)
    // As this solution is not optimal It will give TLE 
    public int smallestRepunitDivByK(int k) {
        if (k%2==0 || k%5==0) return -1;
        BigInteger p = new BigInteger(k+"");
        BigInteger n = new BigInteger("1");
        int len=1;
        while (true){
            if (n.mod(p) ==BigInteger.ZERO) return len ;
            n = n.multiply(BigInteger.TEN).add(BigInteger.ONE);
            len++;

        }
    }

    //BruteForce
    // TC : O(K) 
    // SC : O(1)
    // Pigeon Hole method (Once Look This up)

    /* 
    
    Consider if  k =6 
    The possible remainder we can get are 0 1 2 3 4 5
    Let see if we get the numbers

    1   11  111 1111    11111   111111
    1   5   3   1       5       3                   remainders for the above numbers

    so these are all possible remainder we will get 1 5 3 1 5 3
    Now we have to find relation 

    so while in k cylce if any number repeats then the loop is present 
    and the number is not  divisible

    We use HashSet to keep track
    */

    public int smallestRepunitDivByKApproach2(int k) {
    
        if(k%2==0 || k%5==0) return -1;
        HashSet <Integer> lookup = new HashSet<Integer>();
        int rem =0,len=0;
        for (int i=0; i<k ; i++){
            rem = (rem*10+1)%k;
            len++;

            if (lookup.contains(rem)) return -1;
            if (rem==0) return len;
            lookup.add(rem);
        }
        return -1;
    }

    //BruteForce
    // TC : O(K) 
    // SC : O(1)
    // Pigeon Hole method (Once Look This up)

    /* 
    
    Consider if  k =6 
    The possible remainder we can get are 0 1 2 3 4 5
    Let see if we get the numbers

    1   11  111 1111    11111   111111
    1   5   3   1       5       3                   remainders for the above numbers

    so these are all possible remainder we will get 1 5 3 1 5 3
    Now we have to find relation 

    111 = 11*10 + 1
    modulo of 6 on both sides

    111%6  =  11%6 *10 +1%6
    111%6 = (11*10+1)%6
    next_rem = (prev_rem*10+1) %k

    so if the next_rem is true we return answer if not then that means the number cannot be divided
    */

    public int smallestRepunitDivByKApproach3(int k) {
    
        if(k%2==0 || k%5==0) return -1;
        int rem=0,len=0;
        for (int i=0; i<k ; i++){
            rem = (rem*10+1)%k;
            len++; 
            if (rem==0) return len;

        }
        return -1;
    }
}