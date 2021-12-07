package binarySearch;

// https://leetcode.com/problems/arranging-coins/

public class arrangingCoins {
    public static void main(String[] args) {
        SolutionAC solution = new SolutionAC();
        System.out.println(solution.arrangeCoins(5)); //2
        System.out.println(solution.arrangeCoins(1)); //1
        System.out.println(solution.arrangeCoins(0)); //0
        System.out.println(solution.arrangeCoins(1804289383)); //60070
        System.out.println(solution.arrangeCoinsBruteForce(5));
        System.out.println(solution.arrangeCoinsBruteForce(1804289383));
    }
}

class SolutionAC {

    //TC = O(sqrt(n)) or O(i)
    // SC = O(1)
    public int arrangeCoinsBruteForce(int n){
        long total = 0;
        int i=0;
        while (total <= n){
            total += ++i;
        }
        return i-1;
    }

    // Best Solution 
    // TC = O(log n) 
    // SC = O(1)
    public int arrangeCoins(int n) {
        long start = 0;
        long end = n;
        
        while (start<=end){
            
            long mid = start  + (end - start )/2;
            long total = mid *(mid+1)/2;
            if(total< n) start = mid+1;
            else if (total> n)end = mid-1;
            else return (int)mid;

        }
        return (int)end;
    }
    /*
    Approach 3: Math
    For a given n, we already know that (k(k+1))/2 <= n. We can further simplify this equation:

    (k(k+1))/2 <= n
    k(k+1) <= 2n
    k^2 + k - 2n <= 0 

    By general formula for quadratic equations,

    k <= [ -1 + sqrt( 1^2 - 4*1*(-2n) ) ] / [ 2(1) ]
    k <= [ sqrt(8*n+1) - 1 ] / 2

    This equation takes O(1) time to compute. Hence, we can calculate k directly from n in O(1) time.
    */

    public int arrangeCoinsConstantTime(int n) {
        return (int)(Math.sqrt(8*(long)(n)+1)-1)/2;

    }
}

