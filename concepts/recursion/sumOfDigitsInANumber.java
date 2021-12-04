package concepts.recursion;

public class sumOfDigitsInANumber {
    public static void main(String[] args) {
        System.out.println(summationOfDigits(345));
        System.out.println(summationOfDigits(3423423));
        System.out.println(summationOfDigits(45634));
        System.out.println(summationOfDigits(0));
        System.out.println(summationOfDigits(-1221));
        
    }
    
    public static int summationOfDigits(int n){
        if (n<0) return -1;
        else if (n==0 ) return 0;
        return n%10 + summationOfDigits(n/10);
    }
}
