package concepts.recursion;

public class printNumberFrom1toNAndNto1 {

    public static void main(String[] args) {
        int n = 5;
        printNumbers(n);
    }
    public static void printNumbers(int n){
        if (n<1) return ;
        System.out.println(n);
        printNumbers(n-1);
        System.out.println(n);
    }
    
}
