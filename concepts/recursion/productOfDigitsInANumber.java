package concepts.recursion;

public class productOfDigitsInANumber {
    public static void main(String[] args) {
        System.out.println(productOfDigits(345345));
    }

    public static int productOfDigits(int n){
        if (n%10==n) return n;
        else return n%10 * productOfDigits(n/10); 
    }
}
