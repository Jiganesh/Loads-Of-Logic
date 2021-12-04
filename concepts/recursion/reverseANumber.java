package concepts.recursion;

public class reverseANumber {
    public static void main(String[] args) {
        System.out.println(reverseTheNumber(2343));
        System.out.println(reverseTheNumber(85649889));
        System.out.println(reverseTheNumber(987654321));
    }

    public static int reverseTheNumber(int n){
        if (n %10 ==n) return n;
        return n%10 * (int)Math.pow (10,(int) Math.log10(n)) + reverseTheNumber(n/10);
    }
}