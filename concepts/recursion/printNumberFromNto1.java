package concepts.recursion;

public class printNumberFromNto1 {
    public static void main(String[] args) {
        int n = 5;
        printNumbers(n);
    }
    public static void printNumbers(int n){
        if (n<1) return;
        printNumbers(n-1);
        System.out.println(n);

    }
}
