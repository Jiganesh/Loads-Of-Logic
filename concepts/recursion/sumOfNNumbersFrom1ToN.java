package concepts.recursion;

public class sumOfNNumbersFrom1ToN {
    public static void main(String[] args) {
        int n = 16335467;
        System.out.println(summationInConstantTime(n));
        System.out.println(summation(n)); // not recommended for big numbers
    }

    public static int summation(int n ){
        // Time Complextity : O(N)
        // Space Complexity : O(N) Auxilary stack space
        if (n<=1) return 1;
        else return n  + summation(n-1);
    }



    public static int summationInConstantTime(int n){
        // Time Complexity : O(1)
        // Space Complexity : O(1)
        return n*(n+1)/2;
    }
}
