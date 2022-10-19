
import java.util.Scanner;

public class towerOfHanoi {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int t1 = scn.nextInt();
        int t2 = scn.nextInt();
        int t3 = scn.nextInt();
        toh(n, t1, t2, t3);
    }
    public static void toh(int n,int t1,int t2,int t3) {
        if(n==0){
            return;
        }
        //Will print instructions to move n-1 blocks from A to C without violating the rules .
        toh(n-1,t1,t3,t2);

        // Moving nth block from A to B .
        System.out.println(n+"[" + t1 + "->" + t2 + "]");

        //Will print instructions to move n-1 blocks from C to b without violating the rule .
        toh(n-1,t3,t2,t1);
    }
}
