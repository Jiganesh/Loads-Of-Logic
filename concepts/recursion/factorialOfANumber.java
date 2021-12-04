package concepts.recursion;

public class factorialOfANumber {
    public static void main(String[] args) {
        int  n = 6;
        System.out.println(factorial(n));
    }

    public static int factorial(int n){
        if (n<=1) return 1;
        else return n  * factorial (n-1);
    }
    
}

// n-- pass the number and then decrement
// --n decrement the number and then pass
